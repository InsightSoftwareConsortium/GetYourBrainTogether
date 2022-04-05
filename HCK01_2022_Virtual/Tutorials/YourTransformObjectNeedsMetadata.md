Back to the [Tutorials List](../../README.md#tutorials-list)

# Your Transform Object needs Metadata

## Instructors

- Hastings Greer

## Tutorial Description
    Downstream medical application code needs to correctly handle image spacing, 
    image orientation, and unusual image origins correctly – in particular, landmarks, 
    volume and size measurements, and mesh data are always in physical coordinates.

    If we try to manually handle this metadata by, for each downstream task, manually scaling, 
    transposing, and shifting deformation fields, we will make mistakes and spend a lot of time. 
    Instead, we need to use a metadata-aware representation of image registration 
    results at application boundaries. I propose that itk.Transform objects are the current best option.
    
    [notebook](https://colab.research.google.com/drive/1NAFFGCD2hh84kfkCQpNhSC4wK4v4MVlq?usp=sharing)

## Learning Outcomes

<!-- Describe here what you would like participants to learn by the end of the tutorial. -->

1. Outcome 1. At the end of this tutorial, participants will be able to add a wrapper or interface to their registration project, that
    - Takes as input a pair of ITK images with spatial metadata
    - Outputs an ITK Transform with spatial metadata

2. Outcome 2. Participants will be able to structure a downstream application to use this format, making switching registration libraries achievable

## Approach and Materials

<!-- Describe here how the tutorial will be taught, e.g. slides, Jupyter
notebooks, and provide links to any materials. -->

- [Slides](ITK transforms as registration product.pdf)
- [notebook](https://colab.research.google.com/drive/1NAFFGCD2hh84kfkCQpNhSC4wK4v4MVlq?usp=sharing)
- ...

## Background and References

[https://pypi.org/project/icon-registration/](https://pypi.org/project/icon-registration/)
[ITK](http://github.com/InsightSoftwareConsortium/ITK)

<!-- Provide links to related publications and software repositories here. -->
