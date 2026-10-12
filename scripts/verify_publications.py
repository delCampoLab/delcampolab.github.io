#!/usr/bin/env python3
"""Verify publication pages against Crossref, bioRxiv and PubMed.

For every content/publication/*/index.md with a `doi:`:
  * fetch the Crossref record and compare its title with the page title;
  * fill `publication:` and `pages:` only when they are empty on the page,
    and report differences for filled ones (volume, issue and issued date
    are reported only: the theme has no fields for them, and dates are
    never changed automatically);
  * source the abstract from bioRxiv, then PubMed, then Crossref, and
    replace the page `abstract:` with it.

Writes scripts/publications_audit.md. Pages are only modified with --apply;
without it the script is a dry run that still writes the audit.

Guarantees: never runs `academic import`, never touches `authors:`, `tags:`,
`featured:` or any image, never creates or deletes a page. It edits only the
`abstract:`, `publication:` and `pages:` lines of the front matter.

Usage: python3 scripts/verify_publications.py [--apply] [--only SLUG ...]
"""

import argparse
import difflib
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB_DIR = ROOT / "content" / "publication"
AUDIT = ROOT / "scripts" / "publications_audit.md"
UA = "delcampolab-site-maintenance/1.0 (publication verification script)"
TITLE_MATCH_THRESHOLD = 0.85
EDITABLE_KEYS = ("abstract", "publication", "pages")

# DOIs on the site but not yet in the Zotero library (flag only).
NOT_IN_ZOTERO = {
    "keeling2020letter",
    "reichel2026permits",
    "bonacolta2026single",
    "binsarhan2025microbiome",
}


# --------------------------------------------------------------------------
# HTTP helpers

_last_call = {}


def _throttle(host, min_interval):
    wait = _last_call.get(host, 0) + min_interval - time.time()
    if wait > 0:
        time.sleep(wait)
    _last_call[host] = time.time()


def http_get(url, accept=None, min_interval=0.6, retries=4):
    host = urllib.parse.urlparse(url).netloc
    headers = {"User-Agent": UA}
    if accept:
        headers["Accept"] = accept
    for attempt in range(retries):
        _throttle(host, min_interval)
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=40) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(5 * (attempt + 1))
                continue
            raise
        except (urllib.error.URLError, TimeoutError):
            time.sleep(5 * (attempt + 1))
    return None


# --------------------------------------------------------------------------
# Text helpers

def clean_text(s):
    """Strip JATS/HTML tags and collapse whitespace."""
    s = html.unescape(s or "")
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", clean_text(s).lower().replace("-", " "))


def similarity(a, b):
    a, b = norm(a).split(), norm(b).split()
    if not a and not b:
        return 1.0
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()


def yaml_quote(s):
    """Double-quoted, single-line YAML scalar."""
    s = re.sub(r"\s+", " ", s).strip()
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def yaml_unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        return v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    if len(v) >= 2 and v[0] == "'" and v[-1] == "'":
        return v[1:-1].replace("''", "'")
    return v


def date_str(parts_obj):
    parts = (parts_obj or {}).get("date-parts", [[None]])[0]
    if not parts or parts[0] is None:
        return ""
    return "-".join(f"{p:02d}" if i else str(p) for i, p in enumerate(parts) if p)


# --------------------------------------------------------------------------
# Front matter (line based, so formatting of untouched lines is preserved)

def read_page(path):
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    if lines[0].strip() != "---":
        raise ValueError(f"{path}: no front matter")
    end = lines.index("---", 1)
    fields = {}
    for i in range(1, end):
        m = re.match(r"^([A-Za-z_]+):\s?(.*)$", lines[i])
        if m:
            fields[m.group(1)] = (i, m.group(2))
    return lines, end, fields


def get_field(fields, key):
    return yaml_unquote(fields[key][1]) if key in fields else None


def set_field(lines, fields, key, value):
    assert key in EDITABLE_KEYS, key
    if key not in fields:
        return False
    i, _ = fields[key]
    lines[i] = f"{key}: {yaml_quote(value)}"
    return True


# --------------------------------------------------------------------------
# Sources

def crossref(doi):
    raw = http_get("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/"),
                   accept="application/json")
    return json.loads(raw)["message"] if raw else None


def biorxiv_abstract(doi):
    if not doi.startswith(("10.1101/", "10.64898/")):
        return None
    raw = http_get(f"https://api.biorxiv.org/details/biorxiv/{doi}")
    if not raw:
        return None
    coll = json.loads(raw).get("collection") or []
    return clean_text(coll[-1].get("abstract")) if coll else None


def pubmed_abstract(doi):
    eu = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    q = urllib.parse.urlencode({"db": "pubmed", "term": f"{doi}[AID]", "retmode": "json"})
    raw = http_get(f"{eu}esearch.fcgi?{q}", min_interval=0.4)
    if not raw:
        return None
    ids = json.loads(raw).get("esearchresult", {}).get("idlist", [])
    if len(ids) != 1:
        return None
    raw = http_get(f"{eu}efetch.fcgi?db=pubmed&id={ids[0]}&retmode=xml", min_interval=0.4)
    if not raw:
        return None
    root = ET.fromstring(raw)
    # Make sure the PubMed record really carries this DOI.
    dois = {e.text.strip().lower() for e in root.iter("ArticleId")
            if e.get("IdType") == "doi" and e.text}
    dois |= {e.text.strip().lower() for e in root.iter("ELocationID")
             if e.get("EIdType") == "doi" and e.text}
    if doi.lower() not in dois:
        return None
    parts = [clean_text("".join(e.itertext())) for e in root.iter("AbstractText")]
    text = " ".join(p for p in parts if p)
    return text or None


def crossref_abstract(rec):
    a = clean_text((rec or {}).get("abstract", ""))
    a = re.sub(r"^(Abstract|ABSTRACT|Summary)\s*:?\s+", "", a)
    return a or None


# --------------------------------------------------------------------------

def process(path, apply):
    slug = path.parent.name
    lines, _, fields = read_page(path)
    title = get_field(fields, "title") or ""
    doi = (get_field(fields, "doi") or "").strip()
    row = dict(slug=slug, doi=doi or "-", title_match="-", source="-",
               changed="no", sim="-", other=[], notes=[])
    if slug in NOT_IN_ZOTERO:
        row["notes"].append("DOI not yet in Zotero")
    if not doi:
        row["notes"].append("no DOI: skipped")
        return row

    rec = crossref(doi)
    if rec is None:
        row["notes"].append("DOI not found in Crossref")
    else:
        ctitle = clean_text((rec.get("title") or [""])[0])
        tsim = similarity(title, ctitle)
        row["title_match"] = "yes" if tsim >= TITLE_MATCH_THRESHOLD else "no"
        if row["title_match"] == "no":
            row["notes"].append(f"Crossref title ({tsim:.2f}): {ctitle}")

        journal = clean_text((rec.get("container-title") or [""])[0])
        page_pub = clean_text((get_field(fields, "publication") or "").replace("*", ""))
        if journal:
            if not page_pub:
                if set_field(lines, fields, "publication", f"*{journal}*"):
                    row["other"].append(f"publication filled: *{journal}*")
            elif similarity(page_pub, journal) < 0.8:
                row["other"].append(f"publication differs (Crossref: {journal})")

        cpages = (rec.get("page") or "").replace("--", "-")
        page_pages = get_field(fields, "pages")
        if cpages:
            if page_pages == "":
                if set_field(lines, fields, "pages", cpages):
                    row["other"].append(f"pages filled: {cpages}")
            elif page_pages is not None and page_pages != cpages:
                row["other"].append(f"pages differ (Crossref: {cpages})")

        vol, iss = rec.get("volume"), rec.get("issue")
        if vol or iss:
            row["other"].append(f"vol {vol or '-'}, issue {iss or '-'} (report only)")
        issued = date_str(rec.get("issued"))
        page_date = (get_field(fields, "date") or "")[:10]
        if issued and not page_date.startswith(issued) and not issued.startswith(page_date[:7]):
            row["other"].append(f"date {page_date} vs Crossref issued {issued} (report only)")

    new_abs, source = None, "none"
    for name, fn in (("biorxiv", lambda: biorxiv_abstract(doi)),
                     ("pubmed", lambda: pubmed_abstract(doi)),
                     ("crossref", lambda: crossref_abstract(rec))):
        try:
            new_abs = fn()
        except Exception as e:  # keep going on a bad response
            row["notes"].append(f"{name} error: {e}")
            new_abs = None
        if new_abs:
            source = name
            break
    row["source"] = source

    old_abs = get_field(fields, "abstract")
    if old_abs is None:
        row["notes"].append("page has no abstract field")
    elif new_abs:
        row["sim"] = f"{similarity(old_abs, new_abs):.2f}" if old_abs else "empty"
        if clean_text(old_abs) != clean_text(new_abs):
            set_field(lines, fields, "abstract", new_abs)
            row["changed"] = "yes"
    else:
        row["notes"].append("no abstract source: page abstract left untouched")

    if apply and (row["changed"] == "yes" or any("filled" in o for o in row["other"])):
        path.write_text("\n".join(lines), encoding="utf-8")
    return row


def write_audit(rows, apply):
    out = [
        "# Publications audit",
        "",
        f"Generated by `scripts/verify_publications.py` on {time.strftime('%Y-%m-%d')}"
        f" ({'applied' if apply else 'dry run, pages not modified'}).",
        "",
        "`similarity` compares the old page abstract with the sourced one (word-level, 0–1):"
        " a low value means the page abstract was not the paper's abstract.",
        "",
        "| slug | DOI | title match | abstract source | abstract changed | similarity old→new | other field changes | notes |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        cells = [r["slug"], f"`{r['doi']}`" if r["doi"] != "-" else "-", r["title_match"],
                 r["source"], r["changed"], r["sim"], "; ".join(r["other"]) or "-",
                 "; ".join(r["notes"]) or "-"]
        out.append("| " + " | ".join(c.replace("|", "\\|") for c in cells) + " |")
    AUDIT.write_text("\n".join(out) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--apply", action="store_true", help="write changes to pages")
    ap.add_argument("--only", nargs="*", help="limit to these slugs")
    args = ap.parse_args()
    pages = sorted(PUB_DIR.glob("*/index.md"))
    if args.only:
        pages = [p for p in pages if p.parent.name in set(args.only)]
    rows = []
    for p in pages:
        rows.append(process(p, args.apply))
        r = rows[-1]
        print(f"{r['slug']:32} title={r['title_match']:3} src={r['source']:8} "
              f"changed={r['changed']:3} sim={r['sim']}", file=sys.stderr)
    write_audit(rows, args.apply)
    print(f"wrote {AUDIT.relative_to(ROOT)} ({len(rows)} pages)", file=sys.stderr)


if __name__ == "__main__":
    main()
