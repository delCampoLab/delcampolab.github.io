# CLAUDE.md — del Campo Lab website

Lab website for the del Campo Lab (Microbial Ecology and Evolution, IBE CSIC-UPF, Barcelona).
Live at https://delcampolab.com/ — public-facing, so every push to `main` publishes.

This file is the source of truth for repo mechanics. Strategy, voice, and content
conventions live in the "Lab Website Companion" Claude Project; defer to it for
what to write, and to this file for how to build and ship it.

## Stack

- Hugo extended **0.135.0** (pinned as `WC_HUGO_VERSION` in
  `.github/workflows/publish.yaml`; use the same version locally)
- Hugo Blox Builder, Wowchemy "research-group" theme, pulled as a Hugo Module.
  `go.mod` pins `blox-bootstrap/v5` to commit pseudo-version
  `v5.9.8-0.20241012174104-661cadc17327`. Frozen upstream: do NOT run
  `hugo mod get -u` or attempt theme upgrades unless Javi explicitly asks
- `netlify.toml` and `theme.toml` are template leftovers; deploys do NOT go through Netlify
- Only local theme override: `layouts/partials/site_footer.html`. Touch `layouts/`
  only with explicit approval

## Build, preview, deploy

- Local preview: `hugo server --port 1313 --disableFastRender` from the repo root
  (this is the config in `.claude/launch.json`), then open http://localhost:1313.
  Plain `hugo server` also works
- Production build: `.github/workflows/publish.yaml` runs on every push to `main`
  (plus manual `workflow_dispatch`). It installs hugo_extended 0.135.0, runs
  `hugo --minify --baseURL <pages base URL>`, uploads `./public` as a Pages
  artifact, and deploys with `actions/deploy-pages@v4`. Quirk: the build step runs
  hugo twice, with a debug grep of the theme's `main.scss` in between and `|| true`
  on the first run; harmless, leave it unless cleaning up deliberately
- There is no staging environment. `hugo server` IS the preview. Always preview
  before pushing content changes

## Repo layout

- `content/_index.md` — the homepage. It is a single `type: landing` page whose
  `sections:` list defines the blocks (hero, research-theme tiles, News & Events
  collection, Networks & Initiatives tiles, Recent Publications collection).
  There is NO `content/home/` widget folder in this repo
- `content/post/` — news posts, one folder per post: `YYYY-MM-DD-slug/index.md`
  plus `featured.jpg|png` in the same folder (one legacy folder,
  `2026-04-farewell-matteo`, lacks the day; use the full date for new posts).
  Canonical front matter, matching recent posts:

  ```yaml
  ---
  title: "New paper in PLOS Biology: Symbiotic gut bacteria may drive carbonate production in marine fish"
  date: 2026-05-27
  authors:
    - admin
  image:
    focal_point: 'top'
  ---
  Lead paragraph shown as the summary. 🐟🦠

  <!--more-->

  Full post body…
  ```

  The text before `<!--more-->` is the card summary; recent posts use no
  `summary:` or `tags:` fields
- `content/event/` — events, same folder-per-item pattern. Real template
  (from `2026-04-19-protist2026`):

  ```yaml
  ---
  title: "Protistology Open 2026 — del Campo Lab at PROTIST2026 in Prague"
  event: Protistology Open 2026
  event_url: https://registration.cas.cz/PROTIST2026/
  location: Grand Hotel International, Prague
  address:
    city: Prague
    country: Czech Republic
  summary: One-line summary for cards.
  date: '2026-04-19T09:00:00Z'
  date_end: '2026-04-23T18:00:00Z'
  all_day: true
  publishDate: '2026-04-09T00:00:00Z'
  authors:
    - admin
    - krause
  tags:
    - conference
  featured: true
  image:
    filename: featured.png
    focal_point: Smart
  links:
    - name: Conference website
      url: https://registration.cas.cz/PROTIST2026/
      icon_pack: fas
      icon: globe
  ---
  ```

- `content/publication/` — one folder per paper. Existing folders use
  unhyphenated slugs matching the BibTeX keys (`bonacolta2021starlet`);
  see the publications workflow below before generating anything new
- `content/authors/<slug>/` — one folder per person: `_index.md` + `avatar.jpg`.
  `user_groups` values in use (defined in `content/people/index.md`, sorted by
  `weight`): `Principal Investigators`, `Researchers`, `Grad Students`,
  `Undergrad Students`, `Technicians`, `Visitors`, `Alumni`.
  Author folder slugs don't always match the display `slug:` field
  (folder `agazzi` → slug `matteo-agazzi`); post links use the display slug
  (`/author/matteo-agazzi/`)
- `content/people/index.md` — the People landing page (people block config)
- `content/research/`, `content/project/`, `content/outreach/`,
  `content/art-science/`, `content/contact/`, `content/resources/`
- `config/_default/` — site config, menus, params
- `publications.bib` — master BibTeX file at repo root. Key style:
  `authoryearword`, lowercase, no hyphens (e.g. `gonzalez2008genome`); keep it
- `static/` and `assets/` — media and theme assets

## Publications workflow

The manual procedure below is the only path. The automated
`.github/workflows/import-publications.yml` was deleted in October 2026: it ran
`academic==0.10.0` over the whole of `publications.bib`, which generates
HYPHENATED folder slugs (`bonacolta-2021-starlet`) that duplicate the site's
unhyphenated folders (`bonacolta2021starlet`). Its PR #2 was closed unmerged. Do
not reintroduce a whole-file import.

**Manual procedure for a new paper:**
1. Add the new BibTeX entry to `publications.bib` (keep the existing key style)
2. Copy ONLY the new entry into a temporary file, e.g. `new.bib`, and run
   `academic import new.bib content/publication/ --compact` so nothing existing
   is regenerated. The CLI is NOT installed locally (python3 is miniconda's);
   install once with `python3 -m pip install academic==0.10.0`
3. Rename the generated folder to the unhyphenated key style to match the rest
   of the site, delete `new.bib`
4. Polish the generated `index.md`: in `authors:`, replace each lab member's
   full name with their username (the `content/authors/` folder name, e.g.
   `bonacolta`) so it links to their profile; write the PI exactly as
   `Javier del Campo`; leave external co-authors as plain names. Then check
   abstract rendering, DOI and PDF links, `featured.jpg` if there is one
5. Preview with `hugo server`, confirm the paper shows on /publication/ and the
   homepage Recent Publications block, then commit

## Git conventions

- Work happens directly on `main` (current practice; revisit if Javi prefers
  short-lived branches + PR for bigger changes)
- Commit messages: short imperative subject, e.g. `Add news post: toadfish
  carbonate paper`, `Update Rocío Mozo author page`
- Never force-push, never rewrite published history
- Never delete content folders; move people to alumni via `user_groups`, unpublish
  posts with `draft: true` if ever needed
- Before pushing anything beyond a trivial fix: summarize files touched and what
  changes on the live site, and get Javi's OK

## Gotchas

- Image filenames: Hugo Blox generates hashed variants (`*_hu123...jpg`) under
  `resources/` and `public/`; never edit generated files, only the source image
  in the page bundle
- `public/` and `resources/` are local build output, gitignored and not
  committed; content changes go in `content/`
- Default social sharing image: `assets/media/sharing.jpg` (1200x630). The theme
  looks it up with `resources.GetMatch`, so it must live in `assets/`, not
  `static/`. Pages with a featured image or an author avatar use that instead
- Partner logos (footer, Networks & Initiatives tiles) are served locally from
  `static/media/`; don't hotlink images from external sites
- Emoji render fine in titles and body; the site uses them in news posts
  (🪸🐟🦠, sparingly)
- The site is `en-us`; no multilingual setup
- `.DS_Store` is gitignored; never force-add it
- `.claude/launch.json` holds the hugo server launch config for Claude Code
  sessions; keep it in sync with the preview command above
