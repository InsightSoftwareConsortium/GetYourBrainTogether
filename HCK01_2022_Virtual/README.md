<img alt="Get Your Brain Straight HCK01" src="logos/banner.png">

# Welcome to the web page for the 1st Get Your Brain Straight Hackathon !

## What?

The **Get Your Brain Straight** hackathons **bring together neuroimage data
generators, image registration researchers, and neurodata compute
infrastructure providers for a hands-on, collaborative event**. This community
collaboration aims to **create reproducible, open source resources** that enable
discovery of the structure and function of brains.

There are three components to the hackathon.
First, the primary goal of each hackathon is the generation of a **Reproducible Resource** for registration and analysis of
a specific brain imaging modality.
**Tutorial** sessions share how to work with open source registration tools, open access datasets, or neurodata
archives.
**Birds-of-a-Feather (BOF) Breakout** sessions enable participants
interested in collaborating to work on relevant topics.

**Example ways to participate:**

* [Contribute a registration pipeline resource](https://insightsoftwareconsortium.github.io/GetYourBrainStraight/HCK01_2022_Virtual/#reproducible-resource-challenge) that can be deployed on Brain Imaging Library (BIL) resources to register the challenge dataset.
* [Give a tutorial](https://insightsoftwareconsortium.github.io/GetYourBrainStraight/HCK01_2022_Virtual/#tutorials) about your registration tools. A pre-recorded or live presentation, along with example code and recipes, can teach a data analyst how to run your tool and use the output on the challenge dataset and/or another open dataset.
* [Come and learn](https://insightsoftwareconsortium.github.io/GetYourBrainStraight/HCK01_2022_Virtual/#birds-of-a-feather-breakouts) about registration from experts in the field.

## When, where, how much?

- **Dates:** Monday, April 4th - Thursday, April 7th, 2022

- **Location:** The first hackathon will be online, held on [Zoom](https://alleninstitute-org.zoom.us/j/96111568520?pwd=c2U2UXlFWmdHWVhjWWNUL3V2OWJQZz09) videoconferencing, [Image.sc Island Gather.Town](https://j.mp/imagesc-island) virtual space, and
  [Image.sc Zulip Chat](https://imagesc.zulipchat.com/).

- **Registration:** Fees: none, it's free! Use [this form](https://forms.gle/eJEf7yQq4UeSc1zF9) to register. Deadline: April 2nd.

- **Communication:** to receive information about this and future events please join the [Hackathon Mailing List](https://groups.google.com/g/brain_straight_hackathon_announcements).

## How does it work?

### Before the Hackathon

- [Register](https://forms.gle/eJEf7yQq4UeSc1zF9) for the event. There is no
  cost.
- Sign up for the [mailing list](https://groups.google.com/g/brain_straight_hackathon_announcements).
- [Set up an account](https://www.brainimagelibrary.org/computevisual.html) at the Brain Image Library (BIL).
- Optionally prepare a tutorial or organize a Birds-of-a-Feather (BoF) Breakout, described below.

### During the Hackathon

The week will start 8 AM Pacific Time, 11 AM Eastern Time, Monday, April 4th
in an introductory all-hands videoconference. [recording](https://drive.google.com/file/d/1VpA3F6k9cjyGejRQl8bd9HWuXYQt1zNt/view?usp=sharing).

Following the introduction, participate in the [Reproducible Resource
Challenge](#reproducible-resource-challenge), join the [tutorials](#tutorials), and participate [BoF breakouts](#birds-of-a-feather-breakouts).

On Thursday, 11 AM Pacific Time, 2 PM Eastern Time, participants will delegate one member to present their registration processing pipelines, results, and discuss lessons learned.

## Who can attend?

Get Your Brain Straight hackathons are open to all and publicly advertised. Email announcements are sent to the [mailing list](https://groups.google.com/g/brain_straight_hackathon_announcements).

## Agenda

<div id="calendar-container">
</div>

<!--
Adapted from https://stackoverflow.com/questions/31821974/support-user-time-zone-in-embedded-google-calendar
https://github.com/NA-MIC/ProjectWeek/blob/b4295bddc01542ebb471d57169954b2770fd81fa/PW36_2022_Virtual/README.md
-->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jstimezonedetect/1.0.7/jstz.min.js" integrity="sha512-pZ0i46J1zsMwPd2NQZ4IaL427jXE2RVHMk3uv/wPTNlBVp9AbB1L65/4YdrXRPLEmyZCkY9qYOOsQp44V4orHg==" crossorigin="anonymous"></script>

<!--
<iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FNew_York&mode=WEEK&showNav=0&showTabs=1&showCalendars=0&title=1st%20Get%20Your%20Brain%20Straight%20Hackathon&src=Y18zcjNyNzNycTRpbXN0cjkxMjVxOXY2ZDk4NEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&color=%23F6BF26" style="border:solid 1px #777" width="800" height="600" frameborder="0" scrolling="no"></iframe>
-->
<script type="text/javascript">
  var timezone = jstz.determine();
  var iframe_src = 'https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&mode=WEEK&showNav=0&showTabs=1&showCalendars=0&title=1st%20Get%20Your%20Brain%20Straight%20Hackathon&src=Y18zcjNyNzNycTRpbXN0cjkxMjVxOXY2ZDk4NEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&color=%23F6BF26&dates=20220404%2f20220407&ctz=' + timezone.name()
  var iframe_html = '<iframe src="' + iframe_src + 'style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>'
  document.getElementById('calendar-container').innerHTML = iframe_html;
</script>

[How to add this calendar to your own?](../common/Calendar.md)

## Reproducible Resource Challenge

This aim of this hackathon is to generate reproducible pipelines to register whole-brain microscopy
image data to the [CCFv3](https://doi.org/10.1016/j.cell.2020.04.007). Two datasets are provided,
each with their unique quirks. You may work on either dataset during the hackathon.

In order to work with the neuroimage data generators, these pipelines will take a standardized input
without assumptions of directory structures, filenames, etc and generate standardized outputs.
Expected outputs include: resampled brain, spatial transformation, and a manifest of outputs. The
processing pipelines should be designed to executed in independently in parallel. The output should
be a resampled image with the same size, orientation, and origin as the provided CCFv3. The output
should include an affine transformation file, and a deformation field transformation file to
transform SWC and/or annotation files from the challenge dataset image space into the CCFv3 space.

Criteria for inclusion in a summary paper:

- [ ] Open source with an [OSI-approved license](https://opensource.org/licenses)
    - The code can be executed in the future
    - Researchers can understand what the code is doing
    - Researchers can extend or fix as needed
- Works on open standard data formats used by data providers and consumers
    - [ ] The provided input NIFTI or OME-NGFF images
    - [ ] Provide outputs in open standard formats on the BIL at `/hackathon/2022_GYBS/output/<team-name>/<dataset>/*`.
- Deployable
    - Can be executed across many environments
    - [ ] Provided in a
      published [singularity](https://sylabs.io/guides/2.6/user-guide/introduction.html) image
- [ ] Can be executed by an independent analyst on the BIL

The primary goals for this hackathon is to ensure that everyone's code can run on the dataset
provided and can be replicated.

In future hackathons, we will focus on:

- Combine registration results and methods
- Quantification and characterization of deformation patterns in fMOST imaging
- Identify biologically relevant regions where improvements need to be made
- Focus on accuracy quantification leading to potential improvements

<a name="reproducible-resource-list"/>

[How to add a new reproducible registration processing pipeline?](./ReproducibleResource/README.md)

### Challenge Dataset 1: fMOST Mouse Brain Registration to CCFv3

The fMOST brain volumes and CCFv3 atlas for the hackathon are
available [on the BIL here](https://download.brainlib.org/hackathon/2022_GYBS/input/fMOST/). The input is a
single fMOST NIFTI brain volume. Details about this dataset can be found [here](./Tutorials/fMOSTIntroduction).

### Challenge Dataset 2: Light-Sheet Imaged Mouse Brain Registration to CCFv3

The Light-sheet imaged brain volumes are available
[on the BIL here](https://download.brainlib.org/hackathon/2022_GYBS/input/lightsheet/). For this challenge
set, the data and atlas is provided for a single brain hemisphere (for size considerations and to
mimic most real world experiments). Multiple data replicates are provided. We provide one
dataset `subject0.zarr` in full imaging resolution for those seeking a bigger challenge. As a
convenience we provide the challenge sets at approximately atlas size as
Nifti(`subjectN_25.nii.gz`)
or [OME-NGFF](`subjectN_25.nii.gz`) (`subjectN_25.zarr`). Participants may use either format but
OME-NGFF is preferred because it allows more efficient memory usage for larger datasets.

Details on working with the data can be found 
[here](./Tutorials/MappingLightSheetData/AboutTheDatasets.md)

## Tutorials

Tutorial sessions share how to work with open source registration tools, open access datasets, or neurodata

<a name="tutorials-list"/>

### Monday 4/4

- [Brain Imaging Library (BIL)](https://hackmd.io/@biomed-apps/ryuab8M79), 1 PM-3 PM ET, (Ivan Cao-Berg, Greg Hood, Alex Ropelewski) [recording](https://drive.google.com/file/d/1-1KZmqBX4S1hD52axtSl_TTL7n91WAI6/view?usp=sharing)
- [Get Your Brain Pipelined](./Tutorials/GetYourBrainPipelined), 3 PM ET, (Jeff Duda, Min Chen, Jim Gee) [recording](https://drive.google.com/file/d/1-7ME2zPoV9j3w0zGilGfZG8dg86Lv7Dr/view?usp=sharing)
- [About the Challenge Dataset](./Tutorials/fMOSTIntroduction), 3:30 PM ET, (Lydia Ng) [recording](https://drive.google.com/file/d/1-AML0BjjXWCoLRfs0PJ2XWJxiAaKQhgX/view?usp=sharing)
- [Registering Cleared Tissues](./Tutorials/MappingLightSheetData/MappingLightSheet.md), 4 PM ET, (Ricardo Azevedo) [recording](https://drive.google.com/file/d/1-Lp1D7LHwS1QnU43NESvyTi0lgCejQGd/view?usp=sharing)

### Tuesday 4/5

- [ITKElastix Image Registration Tutorial](./Tutorials/ITKElastixTutorial.md), 10:30-11 AM ET (Viktor van der Valk, Matt McCormick) [recording](https://drive.google.com/file/d/1-Knm-JeY3uEJ7bWS-WEwaFU0YVY4S-_t/view?usp=sharing)
- [Image Registration with a Maximization Minorization (MM) Optimization Algorithm](./Tutorials/MMOptimizationAlgorithm.md), 12:30-1 PM ET (Daniel Tward, Gary Zhou, Ken Langea) [recording](https://drive.google.com/file/d/1-SBAF8_ZPaCNC45EB0wUglEiB5CcDB0W/view?usp=sharing)
- [Metadata Preservation for Image Registration](./Tutorials/MetadataPreservation/MetadataPreservation.md), 1-2 PM ET, (Matt McCormick, Lydia Ng, Dženan Zukić) [recording](https://drive.google.com/file/d/14-Kgt-VoqAHKJHLQBVuOAB-u7w7ve2N4/view?usp=sharing)
- [Your Transform Object Needs Metadata](./Tutorials/YourTransformObjectNeedsMetadata.md), 4-4:45 PM ET (Hastings Greer) [recording](https://drive.google.com/file/d/1-Y1r5MoBOeIgiuAhVd1WR9xggUpwzgtD/view?usp=sharing)

### Wednesday 4/6

- [OME-NGFF: Towards a community standard image file format for sharing big image data in the cloud](https://globalbioimaging.org/international-training-courses/ome-ngff-workshop-2022), 8-11 AM ET, (Christian Tischer, Josh Moore) - *Sister event -- requires additional registration*
- [Mapping Micro to Macro Scale Anatomy with LDDMM](./Tutorials/MappingMicroToMacroScaleAnatomyWithLDDMM.md), 12-1 PM ET, (Kaitlin Stouffer, Bryson Gray, Michael Miller, Daniel Tward)

<a name="how-to-add-a-tutorial"/>

[How to add a new tutorial?](./Tutorials/README.md)

## Birds-of-a-Feather Breakouts

Birds-of-a-Feather (BOF) breakout sessions enable participants
interested in collaborating to work on relevant topics.

To lead or join a Birds-of-a-Feather (BoF) breakout session, create or join a
topic [in this
spreadsheet](https://docs.google.com/spreadsheets/d/1uthoU0CbY-sN5e4neY70IsHKPPXkR21fkcamMDJtmrg/edit#gid=0).
During the BoF, find the leader by clicking on their name in the [Image.sc Island Gather.Town](https://j.mp/imagesc-island) and moving towards their avatar with the keyboard arrow keys. When you are close to their avatar in the virtual space, you will be able to see, hear, and talk to each other.

If notes are taken during the BoF, please add them to the [BoF breakouts
folder](./BoFBreakouts). We recommend [HackMD](https://hackmd.io/) for collaborative,
well-formatted notetaking.

## Code of Conduct

Participants and contributors are expected to adhere to the [ITK Code of Conduct](https://github.com/InsightSoftwareConsortium/ITK/blob/master/CODE_OF_CONDUCT.md).

## Participants

Registered participants:

1. Yufei Chen, AHU
2. oylei, AHU
3. Alice, Allen Institute for Brain Science
4. Pamela Baker, Allen Institute for Brain Science
5. Lydia Ng, Allen Institute for Brain Science
6. Rachel Dalley, Allen Institute for Brain Science
7. Li, Anhui University
8. Yuxiao Zhang, Anhui University
9. tingtinghan, Anhui University
10. Tingting Han, Anhui University
11. Jesse, Anhui University
12. Liyunayuan, Anhui University
13. Iana Vasylieva, Center for Biologic Imaging, University of Pittsburgh
14. Adrian Arias Abreu, Centre for Genomic Regulation
15. Stuart gano, Google
16. John Bogovic, HHMI Janelia
17. Bin Duan, Illinois Tech
18. Can Ceritoglu, JHU Center for Imaging Science
19. Kaitlin Stouffer, Johns Hopkins University
20. Thomas Athey, Johns Hopkins University
21. Brock Wester, Johns Hopkins University Applied Physics Laboratory
22. Erik Johnson, Johns Hopkins University Applied Physics Laboratory
23. Dzenan Zukic, Kitware
24. Tom Birdsong, Kitware
25. Will Schroeder, Kitware
26. Matt McCormick, Kitware
27. Paul Elliott, Kitware
28. Ebrahim Ebrahim, Kitware
29. Viktor van der Valk, LKEB - LUMC
30. Brian Eastwood, MBF Bioscience
31. Kara, N/A
32. Fae Kronman, Penn State University
33. Yongsoo Kim, Penn State University
34. Art Wetzel, Pittsburgh Supercomputing Center
35. Mariah Kenney, Pittsburgh Supercomputing Center
36. Luke Tuite, Pittsburgh Supercomputing Center
37. Greg Hood, Pittsburgh Supercomputing Center / CMU
38. Alexander Ropelewski, PSC
39. Xin Wu, RTI International
40. Zhixi Yun, SEU
41. Adam Aji, SonoVol
42. Yufeng Liu, Southeast University
43. Tony Reksoatmodjo, Translucence Biosystems
44. Kate Lawson, UC Irvine
45. Ricardo Azevedo, UC Irvine
46. Negin, UC Irvine
47. Jaclyn Beck, UC Irvine
48. Zhongkai Wu, UC San Diego
49. Christopher Choi, UCLA
50. Daniel Tward, UCLA
51. Ian Bowman, UCLA BRAIN
52. Luis, UCLA BRAIN
53. Karl Marrett, UCLA Computer Science, VAST lab
54. Guorong Wu, UNC Chapel Hill
55. Hyejin Yang, UNC Chapel Hill
56. Sarah Khan, UNC Chapel Hill
57. Marc Niethammer, UNC Chapel Hill
58. Carolyn McCormick, UNC Chapel Hill
59. Min Chen, University of Pennsylvania
60. Jeffrey Duda, University of Pennsylvania
61. Alan Watson, University of Pittsburgh
62. Nick Tustison, University of Virginia
63. brian, University of Virginia

## Acknowledgements

This hackathon is supported by the National Institute of Mental Health (NIMH) of the National Institutes of Health (NIH) under the [BRAIN Initiative](https://braininitiative.nih.gov/) award numbers [1RF1MH126732](https://projectreporter.nih.gov/project_info_description.cfm?aid=10259930), [1U19MH114830-01](https://projectreporter.nih.gov/project_info_description.cfm?aid=9416007), [5R24MH114793-02](https://reporter.nih.gov/project-details/9567623), [1U24MH114827-01](https://reporter.nih.gov/project-details/9415946) and the [BICCN](https://biccn.org/).
