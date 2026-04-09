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
        
        The **del Campo Lab** is part of the Institute of Evolutionary Biology (CSIC - Universitat Pompeu Fabra) and investigates how corals and their symbiotic microbial partners respond to heat stress under the current climate crisis.
  
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

  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
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

---
