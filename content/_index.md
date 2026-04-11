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
        <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
          <a href="https://delcampolab.com/people/" class="btn btn-primary btn-lg" style="min-width: 180px;">Meet the team</a>
          <a href="https://delcampolab.com/contact/" class="btn btn-primary btn-lg" style="min-width: 180px;">Join the lab</a>
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
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-top: 12px;">
          <div style="border-radius: 12px; padding: 22px 18px; text-align: center; box-shadow: 0 2px 12px rgba(0,0,0,0.07); background: var(--card-bg, #fff);">
            <div style="font-size: 2.4rem; margin-bottom: 10px;">🪸</div>
            <h4 style="margin: 0 0 6px; font-size: 1rem;">Coral Holobiont</h4>
            <p style="margin: 0; font-size: 0.85rem; opacity: 0.72; line-height: 1.5;">How corals and their symbiotic microbes function as an integrated biological system.</p>
          </div>
          <div style="border-radius: 12px; padding: 22px 18px; text-align: center; box-shadow: 0 2px 12px rgba(0,0,0,0.07); background: var(--card-bg, #fff);">
            <div style="font-size: 2.4rem; margin-bottom: 10px;">🌊</div>
            <h4 style="margin: 0 0 6px; font-size: 1rem;">Microbial Diversity</h4>
            <p style="margin: 0; font-size: 0.85rem; opacity: 0.72; line-height: 1.5;">Global patterns in the distribution of marine eukaryotic and prokaryotic microbes.</p>
          </div>
          <div style="border-radius: 12px; padding: 22px 18px; text-align: center; box-shadow: 0 2px 12px rgba(0,0,0,0.07); background: var(--card-bg, #fff);">
            <div style="font-size: 2.4rem; margin-bottom: 10px;">🌡️</div>
            <h4 style="margin: 0 0 6px; font-size: 1rem;">Climate & Heat Stress</h4>
            <p style="margin: 0; font-size: 0.85rem; opacity: 0.72; line-height: 1.5;">Molecular and ecological responses of coral holobionts to rising ocean temperatures.</p>
          </div>
          <div style="border-radius: 12px; padding: 22px 18px; text-align: center; box-shadow: 0 2px 12px rgba(0,0,0,0.07); background: var(--card-bg, #fff);">
            <div style="font-size: 2.4rem; margin-bottom: 10px;">🧬</div>
            <h4 style="margin: 0 0 6px; font-size: 1rem;">Genomics & Bioinformatics</h4>
            <p style="margin: 0; font-size: 0.85rem; opacity: 0.72; line-height: 1.5;">High-throughput sequencing and computational tools to decode microbial symbiosis.</p>
          </div>
        </div>
    design:
      columns: '1'
      spacing:
        padding: ['30px', '0', '10px', '0']

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 16px; padding: 16px 0; text-align: center;">
          <div>
            <div style="font-size: 2.2rem; font-weight: 700; line-height: 1;">6</div>
            <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.6; margin-top: 4px;">Team Members</div>
          </div>
          <div>
            <div style="font-size: 2.2rem; font-weight: 700; line-height: 1;">80+</div>
            <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.6; margin-top: 4px;">Publications</div>
          </div>
          <div>
            <div style="font-size: 2.2rem; font-weight: 700; line-height: 1;">20+</div>
            <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.6; margin-top: 4px;">Lab Alumni</div>
          </div>
          <div>
            <div style="font-size: 2.2rem; font-weight: 700; line-height: 1;">Est. 2019</div>
            <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.6; margin-top: 4px;">Founded</div>
          </div>
        </div>
    design:
      columns: '1'
      spacing:
        padding: ['10px', '0', '20px', '0']

  - block: collection
    content:
      title: News & Events
      subtitle:
      text:
      count: 5
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
        padding: ['60px', '0', '60px', '0']
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
      spacing:
        padding: ['30px', '0', '10px', '0']

---
