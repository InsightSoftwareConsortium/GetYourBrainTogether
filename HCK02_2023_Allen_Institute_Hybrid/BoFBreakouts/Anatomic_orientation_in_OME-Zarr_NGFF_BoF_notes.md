# Get Your Brain Together HCK 02: Anatomic orientation in OME-Zarr NGFF

2023-05-23

## Attendees

- Josh Moore, OME
- David Feng, AIND
- Sharmi, AIND
- Nick TL, Vanderbilt
- Nick Lusk, AIND
- Lydia Ng, AIBS
- Cai McCann,
- Camilo Laiton
- Alan Watson
- Christian
- Christian
- Dzenan Zukic, Kitware
- Beatriz, Cajal Neuro
- Yael Balbastre
- Alan Watson, U Pitt
- Niles, Cajal Neuro
- Satra G, MIT
- Matt McCormick, Kitware

## Discussion

### *Standard, default orientation*?

- LPS?
- RAI?
- RAS? *
- [...]

### Where to store?

- v0.5 later this summer
    - More Transformations
        - Add orientation to Transform Spec
        - https://github.com/ome/ngff/issues/84
        - https://github.com/ome/ngff/pull/138#issuecomment-1467186626
            - Let's merge Affine Transforms GitHub Flash Mob
            - @type
                - Scale
                - AnatomicalToRAS
                - Radial
                - captures more information not captured by current transformations
                - Death to ambiguity
    - Spatial Transcriptomics data storage
        - https://spatialdata.scverse.org/
    - Add to data officially before v0.5 released
    - Propose incremental change to John's transformations proposal may be a good path forward
- New specification
    - Lead authors connection with Josh M
- `axes`, `long_name`
    - https://github.com/ome/ngff/issues/142
    - `long_name` describes axis identifier, direction
- Registration transformations
    - Space names
    - Many registration transformations that mapping to the same anatomic space
        - Define expectations
        - Where and how these are handled
        - Transformations that go beyond rough anatomical orientation go into separate Zarr paths / groups from the multiscale image group
        - Expected sequence or expected conventions for provenance of transformations
    - Do not have to re-write data associated with transformations
        - https://earthmover.io/

### How to standardize?

- Zarr spec?
    - No current mechanism
    - "multiscale" proposed, -> OME spec
        - Geo-Zarr now adding multiscales as "Zarr"
            - https://github.com/zarr-developers/geozarr-spec
            - Spatial concepts
            - May be difficult to converge with OME-Zarr
- OME spec?
- Pubish specification
- Schema that can be validated

### How to encode?

#### Terms relative to the body or the embryonic forebrain 

- https://www.quora.com/Can-you-tell-me-the-key-differences-between-anterior-versus-posterior-ventral-versus-dorsal-and-rostral-versus-caudal-in-terms-of-which-positions-they-are-referring-to-in-anatomical-terminology

#### Direction matrix

- Affine transformation
- Rigid rotation (direction cosines)
- Pre-concatenated (preferred), vs concatenated
- Axis-aligned, human readable metadata
- Nifti, ITK
    - Orientation matrix defines how to rotate into a prescribed orientation
    - S-form and Q-form
        - Has caused confusion
        - Scanner and RAS
        - and this is the set of nifti intent codes: https://nifti.nimh.nih.gov/nifti-1/documentation/nifti1fields/nifti1fields_pages/qsform.html/document_view

Progression, named, concatenated transformation
    1. Scale
    2. Translation
    3. Rough axis-aligned axes, (matrix of 1's, -1's and 0's ?)
    4. Refined orientation / direction matrix

#### Representation, e.g. "LPS", "left-posterior-superior", "left-to-right"

- Towards
    - Nifti to and from discussion
        - https://docs.google.com/document/d/11gCzXOPUbYyuQx8fErtMO9tnOKC3kTWiL9axWkkILNE/edit#heading=h.mqkmyp254xh6
        - some of it was later codified in nitransforms (a python library now): https://nitransforms.readthedocs.io/en/latest/notebooks/isbi2020.html

- Be explicit
- Bring bioimaging and biomedical communities together
    - Try to be inclusive
- Enum
    - Controlled vocabulary
        - https://bids-specification.readthedocs.io/en/stable/appendices/coordinate-systems.html#image-based-coordinate-systems
    - Define translations as needed
- Provenance
    - who defined the transform / coordinate system
    - can you have multiple?
    - are they overwritten? (no yes/no answer; all interpretation)
