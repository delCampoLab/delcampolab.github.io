---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: The symbioses that build a coral
      image:
        filename: welcome.jpg
      text: |
        We investigate how **coral holobionts**—corals and their associated microbes—function and break down under **heat stress**. Focusing on **symbiosis** and **protists**, we use a **systems biology approach** integrating metabarcoding, single-cell and bulk omics, imaging, and AI-driven computational biology. Our goal is to link **symbiont diversity to function** and understand coral responses to the climate crisis.

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; align-items: center;">
          <a href="/people/" class="btn btn-primary btn-lg" style="min-width: 180px;">Meet the team</a>
          <a href="/contact/" class="btn btn-primary btn-lg" style="min-width: 180px;">Join the lab</a>
          <span style="display:inline-flex;align-items:center;gap:10px;">
            <span style="font-weight:600; margin-right:4px; opacity:0.8;">Follow us:</span>
            <a href="https://x.com/delCampoLab" target="_blank" rel="noopener" aria-label="Twitter" class="btn btn-primary btn-lg" style="padding-left:0.75rem;padding-right:0.75rem;">
              <i class="fab fa-twitter"></i>
            </a>
            <a href="https://bsky.app/profile/delcampolab.bsky.social" target="_blank" rel="noopener" aria-label="Bluesky" class="btn btn-primary btn-lg" style="padding-left:0.75rem;padding-right:0.75rem;">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" style="display:block;"><path d="M12 10.8c-1.087-2.114-4.046-6.053-6.798-7.995C2.566.944 1.561 1.266.902 1.565.139 1.908 0 3.08 0 3.768c0 .69.378 5.65.624 6.479.815 2.736 3.713 3.66 6.383 3.364.136-.02.275-.039.415-.056-.138.022-.276.04-.415.056-3.912.58-7.387 2.005-2.83 7.078 5.013 5.19 6.87-1.113 7.823-4.308.953 3.195 2.05 9.271 7.733 4.308 4.267-4.308 1.172-6.498-2.74-7.078a8.741 8.741 0 0 1-.415-.056c.14.017.279.036.415.056 2.67.297 5.568-.628 6.383-3.364.246-.828.624-5.79.624-6.478 0-.69-.139-1.861-.902-2.204-.659-.3-1.664-.62-4.3 1.24C16.046 4.748 13.087 8.687 12 10.8Z"/></svg>
            </a>
            <a href="https://www.instagram.com/delfuegolab/" target="_blank" rel="noopener" aria-label="Instagram" class="btn btn-primary btn-lg" style="padding-left:0.75rem;padding-right:0.75rem;">
              <i class="fab fa-instagram"></i>
            </a>
          </span>
        </div>
    design:
      columns: '1'
      spacing:
        padding: ['20px', '0', '30px', '0']

  - block: markdown
    content:
      title: Research Themes
      subtitle:
      text: |
        <div class="lab-tile-grid">
          <a href="/research/" class="lab-tile">
            <div class="lab-tile__icon">🪸</div>
            <h4 class="lab-tile__title">Coral Holobiont</h4>
            <p class="lab-tile__desc">How corals and their symbiotic microbes function as an integrated biological system.</p>
            <span class="lab-tile__cta">See projects →</span>
          </a>
          <a href="/research/" class="lab-tile">
            <div class="lab-tile__icon">🌊</div>
            <h4 class="lab-tile__title">Microbial Diversity</h4>
            <p class="lab-tile__desc">Global patterns in the distribution of marine eukaryotic and prokaryotic microbes.</p>
            <span class="lab-tile__cta">See projects →</span>
          </a>
          <a href="/research/" class="lab-tile">
            <div class="lab-tile__icon">🌡️</div>
            <h4 class="lab-tile__title">Climate & Heat Stress</h4>
            <p class="lab-tile__desc">Molecular and ecological responses of coral holobionts to rising ocean temperatures.</p>
            <span class="lab-tile__cta">See projects →</span>
          </a>
          <a href="/research/" class="lab-tile">
            <div class="lab-tile__icon">🧬</div>
            <h4 class="lab-tile__title">Genomics & Bioinformatics</h4>
            <p class="lab-tile__desc">High-throughput sequencing and computational tools to decode microbial symbiosis.</p>
            <span class="lab-tile__cta">See projects →</span>
          </a>
        </div>
    design:
      columns: '1'
      spacing:
        padding: ['30px', '0', '10px', '0']


  - block: collection
    content:
      id: news-events
      title: News & Events
      subtitle:
      text:
      count: 4
      filters:
        folders:
          - post
          - event
      offset: 0
      order: desc
    design:
      view: card
      columns: '1'
      spacing:
        padding: ['30px', '0', '30px', '0']

  - block: markdown
    content:
      title: Networks & Initiatives
      subtitle:
      text: |
        <div class="lab-tile-grid">
          <a href="https://demon-protists.eu/" target="_blank" rel="noopener" class="lab-tile">
            <div class="lab-tile__logo">
              <img src="https://demon-protists.eu/wp-content/uploads/2023/05/Logo_DEMON_11_color.png" alt="DEMON">
            </div>
            <h4 class="lab-tile__title">DEMON</h4>
            <p class="lab-tile__desc">European research consortium uncovering protist diversity across marine, freshwater, and terrestrial environments using metabarcoding and omics.</p>
            <span class="lab-tile__cta">Visit website →</span>
          </a>
          <a href="https://medrecover.org/" target="_blank" rel="noopener" class="lab-tile">
            <div class="lab-tile__logo">
              <img src="/media/medrecover-logo.png" alt="MedRecover" onerror="this.style.display='none'">
            </div>
            <h4 class="lab-tile__title">MedRecover</h4>
            <p class="lab-tile__desc">Research initiative on the recovery and resilience of Mediterranean marine ecosystems in the face of climate change and tropicalization.</p>
            <span class="lab-tile__cta">Visit website →</span>
          </a>
          <a href="https://fondationtaraocean.org/en/expedition/tara-coral/" target="_blank" rel="noopener" class="lab-tile">
            <div class="lab-tile__logo">
              <img src="/media/taracoral-logo.png" alt="Tara Coral">
            </div>
            <h4 class="lab-tile__title">Tara Coral</h4>
            <p class="lab-tile__desc">18-month expedition (2026–2028) through the Coral Triangle aboard the schooner <em>Tara</em>, studying coral resistance to global warming.</p>
            <span class="lab-tile__cta">Visit website →</span>
          </a>
          <a href="https://www.biogenoma.cat/" target="_blank" rel="noopener" class="lab-tile">
            <div class="lab-tile__logo">
              <img src="https://www.biogenoma.cat/wp-content/uploads/2021/04/logoverdsenzill2.png" alt="Biogenoma">
            </div>
            <h4 class="lab-tile__title">Biogenoma</h4>
            <p class="lab-tile__desc">Catalan initiative for the Earth BioGenome Project, building a genomic catalog of eukaryotic biodiversity across Catalan-speaking territories.</p>
            <span class="lab-tile__cta">Visit website →</span>
          </a>
          <a href="https://pr2-database.org/" target="_blank" rel="noopener" class="lab-tile">
            <div class="lab-tile__logo">
              <img src="/media/pr2-logo.png" alt="PR2 Database">
            </div>
            <h4 class="lab-tile__title">PR2 Database</h4>
            <p class="lab-tile__desc">Reference database of 18S rRNA sequences for protist metabarcoding, including PR2, PR2-primers, and metaPR2. Dr. del Campo is a core contributor.</p>
            <span class="lab-tile__cta">Visit website →</span>
          </a>
        </div>
    design:
      columns: '1'
      spacing:
        padding: ['30px', '0', '20px', '0']

  - block: collection
    content:
      title: Recent Publications
      text: ""
      count: 5
      filters:
        folders:
          - publication
    design:
      view: citation
      columns: '1'
      spacing:
        padding: ['30px', '0', '10px', '0']

---
