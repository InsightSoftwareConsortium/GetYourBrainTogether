<img alt="Get Your Brain Straight HCK01 Logo" src="logo.png">

# Welcome to the web page for the 1st Get Your Brain Straight Hackathon !

## What?

The **Get Your Brain Straight** hackathons bring together neuroimage data
generators, image registration researchers, and neurodata compute
infrastructure providers for a hand-on, collaborative event. This community
collaboration aims to create reproducible, open source resources that enable
discovery of the structure and function of brains.

There are three components to the hackathon.
First, the primary goal of each hackathon is the generation of a **Reproducible Resource** for registration and analysis of
a specific brain imaging modality.
**Tutorial** sessions share how to work with open source registration tools, open access datasets, or neurodata
archives.
**Birds-of-a-Feather (BOF) Breakout** sessions enable participants
interested in collaborating to work on relevant topics.

## When, where, how much?

- **Dates:** Monday, April 4th - Thursday, April 7th, 2022

- **Location:** The first hackathon will be online, held on [Google
  Meet](https://meet.google.com/) videoconferencing, [Image.sc Island Gather.Town](https://j.mp/imagesc-island) virtual space, and
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
in an introductory all-hands videoconference.

Following the introduction, participate in the [Reproducible Resource
Challenge](#reproducible-resource-challenge-fmost-mouse-brain-registration-to-ccfv3), join the [tutorials](#tutorials), and participate [BoF breakouts](#birds-of-a-feather-breakouts).

On Thursday, 11 AM Pacific Time, 2 PM Eastern Time, participants will delegate one member to present their registration processing pipelines, results, and discuss lessons learned.

## Who can attend?

Get Your Brain Straight hackathons are open to all and publicly advertised. Email announcements are sent to the [mailing list](https://groups.google.com/g/brain_straight_hackathon_announcements).

## Agenda

## Reproducible Resource Challenge: fMOST Mouse Brain Registration to CCFv3

This aim of this hackathon is to generate reproducible pipelines
to register [fMOST mouse
brains](https://knowledge.brain-map.org/data/K1YP17A0QIKJOMOAIS4/summary) to the [CCFv3](https://doi.org/10.1016/j.cell.2020.04.007).

In order to work with the neuroimage data generators, these pipelines will take a standardized input without assumptions of directory structures, filenames, etc and generate standardized outputs.
The input is a single fMOST NIFTI brain volume. Expected outputs include: resampled brain, spatial transformation, and a manifest of outputs.
The processing pipelines should be designed to executed in independently in parallel. The output should be a resampled image with the same size, orientation, and origin as the provided CCFv3.
The output should include an affine transformation file and a deformation field transformation file to transform SWC and/or annotation files from the subject fMOST image space into the CCFv3 space.

Criteria for inclusion in a summary paper:

- [ ] Open source with an [OSI-approved license](https://opensource.org/licenses)
  - The code can be executed in the future
  - Researchers can understand what the code is doing
  - Researchers can extend or fix as needed
- Works on open standard data formats used by data providers and consumers
  - [ ] NIFTI images
- Deployable
  - Can be executed across many environments
  - [ ] Provided in a published [singularity](https://sylabs.io/guides/2.6/user-guide/introduction.html) image
- [ ] Can be executed by an independent analyst on the BIL

The primary goals for this hackathon is to ensure that everyone's code can run on the dataset provided and can be replicated.

In future hackathons, we will focus on:

- Combine registration results and methods
- Quantification and characterization of deformation patterns in fMOST imaging
- Identify biologically relevant regions where improvements need to be made
- Focus on accuracy quantification leading to potential improvements

<a name="reproducible-resource-list"/>

[How to add a new reproducible registration processing pipeline?](./ReproducibleResource/README.md)

## Tutorials

Tutorial sessions share how to work with open source registration tools, open access datasets, or neurodata

<a name="tutorials-list"/>

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

## Acknowledgements

This hackathon is supported by the National Institute of Mental Health (NIMH) of the National Institutes of Health (NIH) under the [BRAIN Initiative](https://braininitiative.nih.gov/) award number [1RF1MH126732](https://projectreporter.nih.gov/project_info_description.cfm?aid=10259930), [1U19MH114830-01](https://projectreporter.nih.gov/project_info_description.cfm?aid=9416007), and the [BICCN](https://biccn.org/).
