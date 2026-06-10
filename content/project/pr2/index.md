---
title: Reference databases for microeukaryote metabarcoding
summary: Building and curating the reference databases — PR2, EukRef, eKOI and more — that turn microeukaryote metabarcoding reads into named, placed, and ecologically meaningful taxa.
tags:
  - Microbial Diversity
  - Genomics & Bioinformatics
  - microbiome
  - metabarcoding
  - phylogenetics
  - microeukaryotes
  - protists
  - database
  - reference databases
  - COI
  - ciliates
date: "2016-04-27T00:00:00Z"

image:
  caption: PR2 taxonomic distribution
  focal_point: Smart

links:
  - icon: globe
    icon_pack: fas
    name: PR2 website
    url: https://pr2-database.org/
  - icon: github
    icon_pack: fab
    name: GitHub
    url: https://github.com/vaulot/pr2_database
  - icon: newspaper
    icon_pack: fas
    name: "Paper: PR2 database"
    url: https://academic.oup.com/nar/article/41/D1/D597/1070586
  - icon: newspaper
    icon_pack: fas
    name: "Paper: EukRef"
    url: https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2004473

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""
---

High-throughput metabarcoding can only describe biodiversity as well as the reference databases used to interpret it. Turning millions of environmental reads into named, placed, and ecologically meaningful taxa depends on carefully curated reference resources — and microbial eukaryotes, the most diverse and least catalogued part of the tree of life, are where that need is most acute. We help build and curate several of these resources, anchored by the PR2 database, and develop the methods and frameworks that turn them into biological insight.

### PR2 and EukRef

The PR2 database was initiated in 2010 in the frame of the BioMarks project, building on work developed over the previous decade in the Plankton Group at the Station Biologique de Roscoff. Its aim is to provide a reference database of carefully annotated 18S rRNA sequences using eight unique taxonomic fields (from kingdom to species). It currently contains over 184,000 sequences, with metadata fields including geo-localisation, culture or environmental origin, host type, and more.

Annotation of PR2 is performed by experts from each taxonomic group. An important partner in this effort is [EukRef](https://eukref.org/), which has merged its bioinformatics pipelines and workshop-based curation efforts with PR2. EukRef has built tools used during multiple workshops dedicated to specific taxonomic groups, including ciliates, choanoflagellates, and others — work that has also produced standalone, phylogeny-based reference databases such as EukRef-Ciliophora, a manually curated SSU rRNA catalogue for one of the most diverse protist phyla.

### Beyond 18S: new markers and groups

The 18S rRNA gene is the workhorse of broad eukaryotic metabarcoding, but it can struggle to separate closely related species. To complement it, we helped build **eKOI**, a curated reference database for the mitochondrial cytochrome oxidase subunit I (COI) gene with a focus on protists. eKOI integrates GenBank and mitochondrial-genome data with extensive manual curation, recovering nearly 16,000 sequences across 80 eukaryotic phyla, and — when used to re-annotate existing COI datasets — surfaces protist diversity that previous surveys had left in the dark.

### From sequences to biology

Well-curated databases also enable better ways of reading the data. Using a PR2-derived reference set of non-bilaterian animal sequences, we have benchmarked 18S phylogenetic-placement approaches — comparing the V4, V9, and full-length barcodes — to recover divergent and hidden lineages more reliably. Looking beyond taxonomy, we are part of efforts to connect these catalogues to organismal biology through a trait-based framework for protist ecology and evolution — a step toward reading metabarcoding data not as lists of taxa but as communities with measurable functions.

**Key publications**

Guillou L, et al. (2013). [The Protist Ribosomal Reference database (PR2): a catalog of unicellular eukaryote small sub-unit rRNA sequences with curated taxonomy](https://academic.oup.com/nar/article/41/D1/D597/1070586). *Nucleic Acids Research* 41:D597–D604.

**del Campo J**, et al. (2018). [EukRef: phylogenetic curation of ribosomal RNA to enhance understanding of eukaryotic diversity and distribution](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2004473). *PLOS Biology* 16:e2005849.

Boscaro V, Santoferrara LF, Zhang Q, Gentekaki E, Syberg-Olsen MJ, **del Campo J**, Keeling PJ (2018). [EukRef-Ciliophora: a manually curated, phylogeny-based database of small subunit rRNA gene sequences of ciliates](https://doi.org/10.1111/1462-2920.14264). *Environmental Microbiology* 20:2218–2230.

González-Miguéns R, Gàlvez-Morante À, Skamnelou M, Antó M, Casacuberta E, Richter DJ, Lara E, Vaulot D, **del Campo J**, Ruiz-Trillo I (2025). [A novel taxonomic database for the eukaryotic mitochondrial cytochrome oxidase subunit I gene (eKOI), with a focus on protist diversity](https://doi.org/10.1093/database/baaf057). *Database* 2025:baaf057.

Jamy M, Ramond P, Bass D, **del Campo J**, Dunthorn M, Lara E, Mitra A, Vaulot D, Santoferrara L (2026). [Towards a trait-based framework for protist ecology and evolution](https://doi.org/10.1016/j.tim.2025.08.008). *Trends in Microbiology* 34:242–251.

Arano-Ansola J, Galan-Luque I, Demenech M, Rico-Martin L, Moody ERR, Suresh M, Vaulot D, **del Campo J**, Giacomelli M, Lozano-Fernandez J (2025). [Evaluating 18S phylogenetic placement accuracy to uncover hidden diversity in early branching animals](https://www.biorxiv.org/content/10.64898/2025.12.09.693319v2). *bioRxiv*.

**Issues and contributions**

Report issues or contribute on [GitHub](https://github.com/vaulot/pr2_database/issues).
