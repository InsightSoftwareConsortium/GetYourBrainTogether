---
name: Schedule a tutorial
about: Describe the tutorial here.
title: "[Tutorial] My tutorial name"
labels: event:HCK03_2024, tutorial
assignees: thewtex

---

body:

name: Schedule a tutorial
description: Describe a tutorial and propose a time
title: "Tutorial: Tutorial Name"
labels: ["tutorial", "event:HCK03_2024_UNC"]
assignees:
  - thewtex

body:

- type: markdown
  attributes:
    value: |
      _Please enter a tutorial name in the title bar above this text. Format: "Tutorial: Tutorial Name"._

- type: markdown
  attributes:
    label: Tutorial description
    description: Describe the purpose and expected learning outcomes of the tutorial.
  validations:
    required: true

- type: dropdown
  attributes:
    label: Duration
    description: Length of the tutorial
    options:
      - 15 minutes
      - 30 minutes
  validations:
    required: true

- type: textarea
  attributes:
    label: Desired time slot
    description: Request time slots in Eastern Time on Friday, July 26th, 2024
    placeholder: |
      1. 9 AM
      1. 10 AM
      1. ...
  validations:
    required: false
