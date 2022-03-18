# Mapping Micro to Macro Scale Anatomy with LDDMM

Note the description below is tentative and may be updated before the event.


## Instructors

- Kaitlin Stouffer (Johns Hopkins University)
- Bryson Gray (UCLA)
- Michael Miller, PhD (Johns Hopkins University)
- Daniel Tward, PhD (UCLA)

## Tutorial Description

<!-- Add a short paragraph describing the tutorial and duration. Recommended
durations is 0.5 to 1.5 hours. -->

Introduction to two concepts central to the field of computational anatomy: (1) the random orbit model used for representing images and (2) large deformation diffeomorphic metric mapping (LDDMM) for mapping images to one another. Variational problems for mapping images of the same modality will be presented (Classic LDDMM), followed by variational problems for mapping images of increasingly different modalities (e.g. different physical dimensions (Projective LDDMM), different contrasts/resolutions (Contrast Transform, Scattering Transform), and different levels of distortion (EM LDDMM)). 

We will demonstrate applying one version of our pipeline to register a multimodal dataset, and describe inputs and outputs. We will also demonstrate an interactive version of our pipeline, via Jupyter notebook, applied to the registration of FMOST data.

Duration: 1.0 hours.

## Learning Outcomes

<!-- Describe here what you would like participants to learn by the end of the tutorial. -->

1. Outcome 1. Familiarity with notation and basics of the random orbit model and LDDMM approach for image registration used by the computational anatomy community.
2. Outcome 2. Awareness of the variety of image registration problems that can now be approached using LDDMM and understanding of the extensions appropriate to each type of problem. 
3. Outcome 3. Ability to run available codes for LDDMM in two of image registration settings: a complex multimodal dataset, and a CCF to FMOST registration task.

## Approach and Materials

<!-- Describe here how the tutorial will be taught, e.g. slides, Jupyter
notebooks, and provide links to any materials. -->

- [Tutorial Slides](https://docs.google.com/presentation/d/14-oOoq1F258Ry8gSaYl_ISLn8R-anW7KXJnKokl95VE/edit#slide=id.g119ae6361ac_0_212)
- [Code Demo Notebooks](https://github.com/twardlab/emlddmm)



## Background and References

<!-- Provide links to related publications and software repositories here. -->
- [LDDMM Reference](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.157.6086&rep=rep1&type=pdf)
- [Projective LDDMM Reference](https://example.com)
- [Projective LDDMM Code](https://github.com/kstouff4/projective-lddmm)
- [EM LDDMM Reference](https://www.frontiersin.org/articles/10.3389/fnins.2020.00052/full)
- [EM LDDMM Code](https://github.com/twardlab/emlddmm)
