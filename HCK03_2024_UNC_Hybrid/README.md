<img alt="Get Your Brain Together HCK03" src="logos/banner.png">

# Welcome to the 3rd Get Your Brain Together Hackathon !

*[Register] now!*

## What?

### Purpose

The **Get Your Brain Together** hackathons **bring together neuroimage data
generators, image registration researchers, and neurodata compute
infrastructure providers for a hands-on, collaborative event**. This community
collaboration aims to **create reproducible, open source resources** that enable
discovery of the structure and function of brains.

This hackathon will focus on **advancing [OME-Zarr] spatial transformations**.

### Motivation

[OME-Zarr] is a cloud-optimized bioimaging file format with international community support and broad adoption across neuroscience. The [current standard] supports large-scale bioimages with spatial metadata. The [coordinate transformations draft] provides a first-class for spatial-transformations in OME-Zarr, which is vitally important for neuroimaging and broader scientific imaging practices to enable:

1. **Reproducibility and Consistency**: Supporting spatial transformations explicitly in a file format ensures that transformations are applied consistently across different platforms and applications. This [FAIR] capability is a cornerstone of scientific research, and having standardized formats and tools facilitates verification of results by independent researchers​​.

2. **Integration with Analysis Workflows**: Having spatial transformations as a first-class citizen within file formats allows for seamless integration with various image analysis workflows. Registration transformations can be used in subsequent image analysis steps without requiring additional conversion.

3. **Efficiency and Accuracy**: Storing transformations within the file format avoids the need for re-sampling each time the data is processed. This reduces sampling errors and preserves the accuracy of subsequent analyses. Standardization enables on-demand transformation, critical for the massive volumes collected by modern microscopy techniques.

4. **Flexibility in Analysis**: A file format that natively supports spatial transformations allows researchers to apply, modify, or reverse transformations as needed for different analysis purposes. This flexibility is critical for tasks such as longitudinal studies, multi-modal imaging, and comparative analysis across different subjects or experimental conditions.

### Agenda

The hackathon is structured into three key components:

1. The first day features **tutorial sessions** designed to impart knowledge on the **application needs** for coordinate transformations, the **mathematical principles** involved, and the **current computational standards and tools** available in the open-source ecosystem.
2. On the second day, small working groups will **review and propose enhancements** to the current [coordinate transformations draft] and [relevant neuroimaging additions].
3. The third day will be dedicated to hands-on activities, during which participants will **implement and apply** the proposed improvements to the standards.

<div id="calendar-container">
</div>

<!--
Adapted from https://stackoverflow.com/questions/31821974/support-user-time-zone-in-embedded-google-calendar
https://github.com/NA-MIC/ProjectWeek/blob/b4295bddc01542ebb471d57169954b2770fd81fa/PW36_2022_Virtual/README.md
-->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jstimezonedetect/1.0.7/jstz.min.js" integrity="sha512-pZ0i46J1zsMwPd2NQZ4IaL427jXE2RVHMk3uv/wPTNlBVp9AbB1L65/4YdrXRPLEmyZCkY9qYOOsQp44V4orHg==" crossorigin="anonymous"></script>

<!--
<iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FNew_York&mode=AGENDA&showNav=0&showTabs=1&showCalendars=0&title=1st%20Get%20Your%20Brain%20Together%20Hackathon&src=Y18zcjNyNzNycTRpbXN0cjkxMjVxOXY2ZDk4NEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&color=%23F6BF26" style="border:solid 1px #777" width="800" height="600" frameborder="0" scrolling="no"></iframe>
-->
<script type="text/javascript">
  var timezone = jstz.determine();
  var iframe_src = 'https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&mode=MONTH&showNav=0&showTabs=1&showCalendars=0&title=2nd%20Get%20Your%20Brain%20Together%20Hackathon&src=Y18zcjNyNzNycTRpbXN0cjkxMjVxOXY2ZDk4NEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&color=%23F6BF26&dates=20240726%2f20240728&ctz=' + timezone.name()
  var iframe_html = '<iframe src="' + iframe_src + 'style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>'
  document.getElementById('calendar-container').innerHTML = iframe_html;
</script>

[How to add this calendar to your own?](../common/Calendar.md)

## When, where, how much?

- **Dates:**
  * Friday, July 26th - Sunday, July 28th, 2024
  * Attend all or part of one of the days
  * Details in the calendar below

- **Location:** The second hackathon will be a _hybrid in-person and online event_, held:
  * On [Google Meet videoconferencing](https://meet.google.com/jtd-ckkd-xjf)
  * At the [University of North Carolina-Chapel
    Hill](https://www.unc.edu/visitors/).
    - [FB141](https://cs.unc.edu/resources/floor-plans/) in the [Brooks Building](https://maps.app.goo.gl/MDhVecvbmMfXYryu9) (Computer Science across the street from the Carolina Inn)
    - <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3231.5231590711087!2d-79.0556608864898!3d35.90969261727207!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89acc2e6203bf08f%3A0xfa61493fe6d88565!2sS%20Columbia%20St%20Brooks%20Computer%20Science%20Building%2C%20Chapel%20Hill%2C%20NC%2027599!5e0!3m2!1sen!2sus!4v1721838603113!5m2!1sen!2sus" width="300" height="250" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  * [Image.sc Island Gather.Town](https://j.mp/imagesc-island) virtual space (see this quick [Intro to Gather Town](https://docs.google.com/document/d/1QeDJXPKSdcRAINPeCNnWcNmVlCfjrc5abrHnEG39ABA/edit?usp=sharing), and
  * [Image.sc Zulip Chat](https://imagesc.zulipchat.com/#narrow/stream/446321-.5B2024-07.5D-Get-Your-Brain-Together-Hackathon-03).

If travelling to attend in-person nearby hotels include:

  * [Hampton Inn & Suites, Chapel Hill](https://www.hilton.com/en/hotels/rducohx-hampton-suites-chapel-hill-carrboro-downtown/?SEO_id=GMB-AMER-HX-RDUCOHX&y_source=1_MjA4Mzg2Mi03MTUtbG9jYXRpb24ud2Vic2l0ZQ%3D%3D)
  * [The Carolina Inn, Chapel Hill](https://www.hyatt.com/en-US/hotel/north-carolina/the-carolina-inn/rdudc?src=corp_lclb_gmb_seo_rdudc)

- **Lead organizers / contacts:** Matt McCormick (Kitware), Marc Niethammer (UNC)

- **Cost:** *[Registration] is free!*

## How does it work?

### Before the Hackathon

- [Register] for the event.
- Sign up for the [mailing list](https://groups.google.com/g/brain_straight_hackathon_announcements).
- Optionally [prepare a tutorial](https://github.com/InsightSoftwareConsortium/GetYourBrainTogether/issues/new?assignees=thewtex&labels=tutorial%2Cevent%3AHCK03_2024_UNC&projects=&template=schedule-a-tutorial.yml&title=Tutorial%3A+My+tutorial+name).

### Who can attend?

Get Your Brain Together hackathons are open to all and publicly advertised. Email announcements are sent to the [mailing list](https://groups.google.com/g/brain_straight_hackathon_announcements).

## Tutorials

<a name="tutorials-list"/>

[Tutorials Video Recording](https://drive.google.com/file/d/16smj-D7b2bPdYVY7feaHCvMgiPAEKj1m/view?usp=sharing)
[Tutorial Transcript](https://docs.google.com/document/d/1UC4mHTv1_gcsEmLRRzY1E-CyRhlZ5aZmBYWOYyfEBs0/edit?usp=sharing)

### Friday 7/26

[Giotto Spatial Transforms](./giotto_spatial_transforms.html) - 9:00 AM ET - Jiaji Chen (George) - Boston University
: Spatial transformations of data will become more and more important in the near future due to the fact that performing spatial analyses across any two sections of tissue from the same block will require that data to be spatially aligned into a common coordinate space. Minute differences during the sectioning process from the cutting motion to how long an FFPE section was floated can result in even neighboring sections being distorted when compared side-by-side.
: These differences make it difficult to assemble multislice and/or cross platform multimodal datasets into a cohesive 3D volume. The solution for this is to perform registration across either the dataset images or expression information. Based on the registration results, both the raster images and vector feature and polygon information can be aligned into a continuous whole.
: Ideally this registration will be a free deformation based on sets of control points or a deformation matrix, however affine transforms already provide a good approximation. In either case, the transform or deformation applied must work in the same way across both raster and vector information.
: Giotto provides spatial classes and methods for easy manipulation of data with 2D affine transformations. These functionalities are all available from `GiottoClass`.

MONAI Lazy Transforms and Geometric Transforms Proposal Discussion - 9:30 AM ET - Benjamin Murray, King's College London 
: Discuss how multiple coordinate transformations are deferred for computation in [MONAI](https://monai.io) and the proposal for Geometric Transforms.

[An implementation decoupling the storage representation from the in-memory representation](./decoupling_in_memory_from_disk.pdf) - 10:00 AM ET - Luca Marconato, EMBL 
: Within the [SpatialData](https://github.com/scverse/spatialdata/) library (a Python package for representing and processing spatial molecular datasets), we needed a way to represent vector and raster data across coordinate systems and store affine and non-linear coordinate transformations between them. We also needed to store this information in a language-agnostic way, so we decided to rely on the NGFF specification to represent the data.
: Our first implementation was in the form of classes modeled closely after the NGFF design. While optimal for read/write operations, we soon realized that our API requirements needed to differentiate between the on-disk and in-memory representation.
: In the tutorial, we will discuss the lessons learned, the "selling points" and the limitations of our APIs, and the "behind the scenes", showing some technical details of our current implementation. We will also discuss a planned refactoring that will create a bridge between NGFF transformations and the xarray system of representing data coordinates.

napari-spatialdata - 10:30 AM ET - Wouter-Michiel Adrien Maria Vierdag, EMBL

BigWarp and Ome-Zarr: a match made in Fiji - 11:00 AM ET - John Bogovic, Janelia Research
: BigWarp is a Fiji / Java tool for manual, deformable 2D and 3D image registration. This tutorial will highlight the ways BigWarp uses the draft transformation specification for import and export. In particular, I will show a use case where, given a moving image, a target image, and a set of transformations, bigwarp automatically determines which transformations to apply, in what direction (forward or inverse), and in what order. We will discuss how the Ome-Zarr transformation specification enables this functionality. If there is time and interest, I will show how BigWarp interpolates two transformations using a mask image, and how decomposing transformations into parts results in nicer behavior.

Making Meaningful (Mouse) Mappings - 11:30 AM ET - Nick Tustison - University of Virginia
: The Advanced Normalization Tools Ecosystem (ANTsX) is a comprehensive open-source software toolkit for generalized quantitative imaging with applicability to multiple organ systems, modalities, and animal species. In this tutorial, we illustrate the utility of ANTsX for generating precision spatial mappings of the mouse brain.   Specifically we discuss two recently developed ANTsX tools:

* The modeling of a velocity flow-based mapping spanning the spatiotemporal domain of a longitudinal trajectory which we apply to the Developmental Common Coordinate Framework—a longitudinal atlas demonstrating mouse development. 
* An automated structural morphological pipeline for determining volumetric and cortical thickness measurements analogous to the well-utilized ANTsX pipeline for human neuroanatomical structural morphology which  illustrates a general open-source framework for tailored brain parcellations.

Fully functional examples of the above are provided at a [dedicated GitHub repository](https://github.com/ntustison/ANTsXMouseBrainMapping) meant to accompany our recent [preprint](https://www.biorxiv.org/content/10.1101/2024.05.01.592056v1).  The tutorial will be given using the [ANTsPy toolkit](https://github.com/ANTsX/ANTsPy) with functionality self-contained tutorials [available](https://tinyurl.com/antsxtutorial).

Your Transform Object needs Metadata - 1:00 PM ET - Thomas Hastings Greer - University of North Carolina-Chapel Hill
: Downstream medical application code needs to correctly handle image spacing, image orientation, and unusual image origins correctly – in particular, landmarks, volume and size measurements, and mesh data are always in physical coordinates.
: If we try to manually handle this metadata by, for each downstream task, manually scaling, transposing, and shifting deformation fields, we will make mistakes and spend a lot of time. Instead, we need to use a metadata-aware representation of image registration results at application boundaries. I propose that itk.Transform objects are the current best option.

Transformations in the Visualization Toolkit (VTK) - 1:45 PM ET Andras Lasso - Queens University

## Code of Conduct

Participants and contributors are expected to adhere to the [ITK Code of Conduct](https://github.com/InsightSoftwareConsortium/ITK/blob/master/CODE_OF_CONDUCT.md).

## Acknowledgements

This hackathon is supported by the National Institute of Mental Health (NIMH) of the National Institutes of Health (NIH) under the [BRAIN Initiative](https://braininitiative.nih.gov/) award numbers [1RF1MH126732](https://projectreporter.nih.gov/project_info_description.cfm?aid=10259930).

[OME-Zarr]: http://dx.doi.org/10.1007/s00418-023-02209-1
[current standard]: https://ngff.openmicroscopy.org/latest/
[coordinate transformations draft]: https://github.com/ome/ngff/pull/138
[relevant neuroimaging additions]: https://github.com/ome/ngff/issues/208
[FAIR]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4792175/
[Registration]: https://forms.gle/LL4quQsbSWawKYSa6
[Register]: https://forms.gle/LL4quQsbSWawKYSa6
