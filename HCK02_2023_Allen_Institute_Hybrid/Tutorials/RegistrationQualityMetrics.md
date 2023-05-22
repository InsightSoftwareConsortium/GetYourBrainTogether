Back to the [Tutorials List](../../README.md#tutorials-list)

# Tutorial: Registration Quality Metrics

## Instructors

- Tom Birdsong (Kitware)

## Tutorial Description

<!-- Add a short paragraph describing the tutorial and duration. Recommended
durations is 0.5 hours. -->

An image registration pipeline produces a relationship mapping from a moving
to a fixed image space. How do we evaluate the accuracy of that relationship?
What data can we use to define investigative paths for iterating on results? In this tutorial
we will examine these questions along with tooling considerations for evaluating
registration outcomes.

Duration: 0.5 hours.

## Learning Outcomes

<!-- Describe here what you would like participants to learn by the end of the tutorial. -->

1. Outcome 1. Learn common spatial considerations for evaluating registered image annotations.
2. Outcome 2. Learn a voxel-based overlap approach to registration evaluation.
3. Outcome 3. Learn a point-set-based approach to registration evaluation.

## Approach and Materials

<!-- Describe here how the tutorial will be taught, e.g. slides, Jupyter
notebooks, and provide links to any materials. -->

- [Slides](https://docs.google.com/presentation/d/1RPNxXeeA4PTFTzkU6MtYzRQSxojSDxvj3R2qoasawlY/)
- [Label Comparison in Neuroglancer](https://aind-neuroglancer-sauujisjxq-uw.a.run.app/#!%7B%22dimensions%22:%7B%22x%22:%5B0.001%2C%22m%22%5D%2C%22y%22:%5B0.001%2C%22m%22%5D%2C%22z%22:%5B0.000025%2C%22m%22%5D%7D%2C%22position%22:%5B5.4431633949279785%2C-6.948322296142578%2C-121.05714416503906%5D%2C%22crossSectionScale%22:1.0959898747034342%2C%22projectionOrientation%22:%5B0.33179789781570435%2C-0.2045859545469284%2C-0.6713171601295471%2C0.6303871870040894%5D%2C%22projectionScale%22:1055.1816132480824%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22zarr://s3://aind-kitware-collab/SmartSPIM_652506_2023-01-09_10-18-12_stitched_2023-01-13_19-00-54/registered/Ex_561_Em_593/processed/2023.04.17/elastix_registered_25um.zarr/%22%2C%22transform%22:%7B%22matrix%22:%5B%5B0%2C-1%2C0%2C0%5D%2C%5B0%2C0%2C-1%2C0%5D%2C%5B1%2C0%2C0%2C0%5D%5D%2C%22outputDimensions%22:%7B%22z%22:%5B0.000025%2C%22m%22%5D%2C%22y%22:%5B0.001%2C%22m%22%5D%2C%22x%22:%5B0.001%2C%22m%22%5D%7D%7D%7D%2C%22tab%22:%22rendering%22%2C%22shaderControls%22:%7B%22normalized%22:%7B%22range%22:%5B0%2C255%5D%2C%22window%22:%5B0%2C255%5D%7D%7D%2C%22name%22:%22elastix_registered_25um.zarr%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22zarr://s3://aind-kitware-collab/SmartSPIM_652506_2023-01-09_10-18-12_stitched_2023-01-13_19-00-54/registered/annotations/processed/2023.04.28/LSh_7n_registered.zarr%22%2C%22transform%22:%7B%22matrix%22:%5B%5B0%2C-1%2C0%2C0%5D%2C%5B0%2C0%2C-1%2C0%5D%2C%5B1%2C0%2C0%2C0%5D%5D%2C%22outputDimensions%22:%7B%22z%22:%5B0.000025%2C%22m%22%5D%2C%22y%22:%5B0.001%2C%22m%22%5D%2C%22x%22:%5B0.001%2C%22m%22%5D%7D%7D%7D%2C%22tab%22:%22source%22%2C%22blend%22:%22additive%22%2C%22name%22:%22LSh_7n_registered.zarr%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22zarr://s3://aind-kitware-collab/SmartSPIM_652506_2023-01-09_10-18-12_stitched_2023-01-13_19-00-54/registered/annotations/processed/2023.04.28/LSh_MHn_registered.zarr%22%2C%22transform%22:%7B%22matrix%22:%5B%5B0%2C-1%2C0%2C0%5D%2C%5B0%2C0%2C-1%2C0%5D%2C%5B1%2C0%2C0%2C0%5D%5D%2C%22outputDimensions%22:%7B%22z%22:%5B0.000025%2C%22m%22%5D%2C%22y%22:%5B0.001%2C%22m%22%5D%2C%22x%22:%5B0.001%2C%22m%22%5D%7D%7D%7D%2C%22tab%22:%22rendering%22%2C%22blend%22:%22additive%22%2C%22shaderControls%22:%7B%22normalized%22:%7B%22range%22:%5B0%2C2%5D%2C%22window%22:%5B0%2C2%5D%7D%7D%2C%22name%22:%22LSh_MHn_registered.zarr%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%7B%22url%22:%22precomputed://s3://aind-kitware-collab/converted_mouse_ccf/annotation/ccf_2017/neuroglancer_ccf_10um%22%2C%22transform%22:%7B%22matrix%22:%5B%5B1%2C0%2C0%2C0%5D%2C%5B0%2C0%2C-1%2C0%5D%2C%5B0%2C-1%2C0%2C0%5D%5D%2C%22outputDimensions%22:%7B%22x%22:%5B0.001%2C%22m%22%5D%2C%22y%22:%5B0.001%2C%22m%22%5D%2C%22z%22:%5B0.000025%2C%22m%22%5D%7D%7D%7D%2C%22tab%22:%22source%22%2C%22name%22:%22CCF%20v3.1%2010um%22%7D%5D%2C%22selectedLayer%22:%7B%22layer%22:%22elastix_registered_25um.zarr%22%7D%2C%22layout%22:%224panel%22%2C%22layerListPanel%22:%7B%22visible%22:true%7D%7D)

## Background and References

<!-- Provide links to related publications and software repositories here. -->

- [Reference registration pipeline Code Ocean Capsule](https://codeocean.allenneuraldynamics.org/capsule/5051231/tree/v2)
