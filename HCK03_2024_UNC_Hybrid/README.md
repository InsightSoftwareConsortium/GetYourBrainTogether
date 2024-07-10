<img alt="Get Your Brain Together HCK03" src="logos/banner.png">

# Welcome to the 3rd Get Your Brain Together Hackathon !

## What?

### Purpose

The **Get Your Brain Together** hackathons **bring together neuroimage data
generators, image registration researchers, and neurodata compute
infrastructure providers for a hands-on, collaborative event**. This community
collaboration aims to **create reproducible, open source resources** that enable
discovery of the structure and function of brains.

This hackathon will focus on **advancing [OME-Zarr] spatial transformations**.

### Motivation

[OME-Zarr] is a cloud-optimized bioimaging file format with international community support and broad adoption across neuoscience. The [current standard] supports large-scale bioimages with spatial metadata. The [coordinate transformations draft] provides a first-class for spatial-transformations in OME-Zarr, which is vitally important for neuroimaging and broader scientific imaging practices to enable:

1. **Reproducibility and Consistency**: Supporting spatial transformations explicitly in a file format ensures that transformations are applied consistently across different platforms and applications. This [FAIR] capability is a cornerstone of scientific research, and having standardized formats and tools facilitates verification of results by independent researchers​​.

2. **Integration with Analysis Workflows**: Having spatial transformations as a first-class citizen within file formats allows for seamless integration with various image analysis workflows. Registration transformations can be used in subsequent image analysis steps without requiring additional conversion. 

3. **Efficiency and Accuracy**: Storing transformations within the file format avoids the need for re-sampling each time the data is processed. This reduces sampling errors and preserves the accuracy of subsequent analyses. Standardization enables on-demand transformation, which is critical for the massive volumes collected by modern microscopy techniques.

4. **Flexibility in Analysis**: A file format that natively supports spatial transformations allows researchers to apply, modify, or reverse transformations as needed for different analysis purposes. This flexibility is critical for tasks such as longitudinal studies, multi-modal imaging, and comparative analysis across different subjects or experimental conditions.

### Hackathon agenda

The hackathon is structured into three key components:

1. The first day features **tutorial sessions** designed to impart knowledge on the **application needs** for coordinate transformation, the **mathematical principles** involved, and the **current computational standards and tools** available in the open-source ecosystem.
2. On the second day, small working groups will **review and propose enhancements** to the current [coordinate transformations draft] and [relevant neuroimaging additions].
3. The third day will be dedicated to hands-on activities, where participants will **implement and apply** the proposed improvements to the standards.

## When, where, how much?

- **Dates:**
  * Friday, July 26th - Sunday, July 28th, 2024
  * Details in the calendar below

- **Location:** The second hackathon will be a hybrid in-person and online event, held:
  * At the [University of North Carolina-Chapel
    Hill](https://www.unc.edu/visitors/) in the Fred Brooke.
  * On Google Meet videoconferencing - link is sent via email to registered participants.
  * [Image.sc Island Gather.Town](https://j.mp/imagesc-island) virtual space (see this quick [Intro to Gather Town](https://docs.google.com/document/d/1QeDJXPKSdcRAINPeCNnWcNmVlCfjrc5abrHnEG39ABA/edit?usp=sharing), and
  * [Image.sc Zulip Chat](https://imagesc.zulipchat.com/).


[OME-Zarr]: http://dx.doi.org/10.1007/s00418-023-02209-1
[current standard]: https://ngff.openmicroscopy.org/latest/
[coordinate transformations draft]: https://github.com/ome/ngff/pull/138
[FAIR]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4792175/