---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        del Campo Lab
      image:
        filename: welcome.jpg
      text: |
        <br>

        We investigate how **corals and their microbial partners** respond to heat stress in a changing ocean — combining genomics, bioinformatics, and global fieldwork to understand and protect marine ecosystems.

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; margin-top: 8px;">
          <a href="https://delcampolab.com/people/" class="btn btn-primary btn-lg" style="min-width: 180px;">Meet the team</a>
          <a href="https://delcampolab.com/contact/" class="btn btn-primary btn-lg" style="min-width: 180px;">Join the lab</a>
        </div>
    design:
      columns: '1'

  - block: markdown
    content:
      title: Research Themes
      subtitle:
      text: |
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-top: 16px;">
          <div style="border-radius: 12px; padding: 28px 20px; text-align: center; box-shadow: 0 2px 12px rgba(0,0,0,0.07); background: var(--card-bg, #fff);">
            <div style="font-size: 2.8rem; margin-bottom: 12px;">🪸</div>
            <h4 style="margin: 0 0 8px; font-size: 1.05rem;">Coral Holobiont</h4>
            <p style="margin: 0; font-size: 0.88rem; opacity: 0.75; line-height: 1.5;">How corals and their symbiotic microbes function as an integrated biological system.</p>
          </div>
          <div style="border-radius: 12px; padding: 28px 20px; text-align: center; box-shadow: 0 2px 12px rgba(0,0,0,0.07); background: var(--card-bg, #fff);">
            <div style="font-size: 2.8rem; margin-bottom: 12px;">🌊</div>
            <h4 style="margin: 0 0 8px; font-size: 1.05rem;">Microbial Diversity</h4>
            <p style="margin: 0; font-size: 0.88rem; opacity: 0.75; line-height: 1.5;">Global patterns in the distribution of marine eukaryotic and prokaryotic microbes.</p>
          </div>
          <div style="border-radius: 12px; padding: 28px 20px; text-align: center; box-shadow: 0 2px 12px rgba(0,0,0,0.07); background: var(--card-bg, #fff);">
            <div style="font-size: 2.8rem; margin-bottom: 12px;">🌡️</div>
            <h4 style="margin: 0 0 8px; font-size: 1.05rem;">Climate & Heat Stress</h4>
            <p style="margin: 0; font-size: 0.88rem; opacity: 0.75; line-height: 1.5;">Molecular and ecological responses of coral holobionts to rising ocean temperatures.</p>
          </div>
          <div style="border-radius: 12px; padding: 28px 20px; text-align: center; box-shadow: 0 2px 12px rgba(0,0,0,0.07); background: var(--card-bg, #fff);">
            <div style="font-size: 2.8rem; margin-bottom: 12px;">🧬</div>
            <h4 style="margin: 0 0 8px; font-size: 1.05rem;">Genomics & Bioinformatics</h4>
            <p style="margin: 0; font-size: 0.88rem; opacity: 0.75; line-height: 1.5;">High-throughput sequencing and computational tools to decode microbial symbiosis.</p>
          </div>
        </div>
    design:
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 24px; padding: 32px 0; text-align: center;">
          <div>
            <div style="font-size: 2.4rem; font-weight: 700; line-height: 1;">6</div>
            <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.65; margin-top: 4px;">Team Members</div>
          </div>
          <div>
            <div style="font-size: 2.4rem; font-weight: 700; line-height: 1;">80+</div>
            <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.65; margin-top: 4px;">Publications</div>
          </div>
          <div>
            <div style="font-size: 2.4rem; font-weight: 700; line-height: 1;">20+</div>
            <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.65; margin-top: 4px;">Lab Alumni</div>
          </div>
          <div>
            <div style="font-size: 2.4rem; font-weight: 700; line-height: 1;">Est. 2019</div>
            <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.65; margin-top: 4px;">Founded</div>
          </div>
        </div>
    design:
      columns: '1'

  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 6
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '2'

  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image:
          filename: parazoo.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

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

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        <div style="text-align: center; padding: 8px 0 24px;">
          <a href="/publication/" class="btn btn-outline-primary">View all publications →</a>
        </div>
    design:
      columns: '1'
---
