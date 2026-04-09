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
      columns: '1'
  
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

  - block: markdown
    content:
      title: Publications
      subtitle:
      text: |
        Browse our full list of publications and preprints on Google Scholar.

        {{% cta cta_link="https://scholar.google.com/citations?user=Mty5iQYAAAAJ&hl=en" cta_text="View publications →" %}}
    design:
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
