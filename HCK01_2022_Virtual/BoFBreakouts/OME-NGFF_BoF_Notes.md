# 1st GYBS OME-NGFF BoF Notes

## Attendees

- John Bogovic
- Lydia Ng
- Iana Vasylieva
- Ebrahim Ebrahim
- Hastings Greer
- Dženan Zukić
- Paul Elliott
- Tom Birdsong
 
## OME-NGFF spec

- https://ngff.openmicroscopy.org/latest/

## Xarray / OME-Zarr compatibility

Dask / xarray support

- https://docs.xarray.dev/en/stable/
https://github.com/astropenguin/xarray-dataclasses
- https://github.com/spatial-image/spatial-image-ngff

- Contribute to the ome-ngff transform discussion
  - https://github.com/ome/ngff/issues/94 
  - 
  

## Current and next standards

- v0.4 (released)
    - scale
    - transformation
    - units
- v0.5 (next)
    - affine
    - displacementfield
    - ...
    - spaces / coordinate systems
    - rigid rotation
        - multiple-representations?
        - Conversion reference library / representation conversion library
        - Linear and displacement field


## Other considerations

* decomposing an affine into sub componsents (scale/rotation)
  * there are ambiguities
* Warnings when crucial metadata is missing
* Provide a UI / interface to make it easy to fix metadata

* please do path-finding for book-keeping lists of transformations -John
  *  Lydia on board
  *  Matt on board
* arrays should always have a spacing and translation -Matt
  * users need and want to see them -Lydia
  * do we have different "names" for transformations that describe array<>physical
  * Organization / association with usability / mental models: grouped image spacing-mental
* A python implementation of generating ome-ngff images with xarray metadata -Matt