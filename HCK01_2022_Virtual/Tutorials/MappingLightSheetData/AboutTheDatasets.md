## Information on Light-sheet datasets

### Directory Structure

All files required for light sheet alignment can be found in:
`hackathon/2022_GYBS/input/lightsheet`

The atlas you will register to is provided in nifti form:
`hackathon/2022_GYBS/input/lightsheet/reference/average_template_25_mm_half.nii.gz`

The datasets you will register to the atlas are found in:
`hackathon/2022_GYBS/input/lightsheet/subject/`
These are provided at the same resolution as the atlas (25um/vox) in nifti files. We provide 6
replicates. They are named `subject{i}_25.nii.gz`. 

Nifti is seldom used in light-sheet microscopy
because it does not play nice with very large files. Therefore, we provide the same data as NGFF
files in the same folder. These are named `subject{i}_25.zarr`. It is preferred you use these
datasets. These zarr files also contain a resolution pyramid if you need it. If you would like to
understand how the metadata is laid out in this data, take a look at the spec
[here](https://ngff.openmicroscopy.org/latest/).

For those looking for an extra challenge, a full resolution dataset is provided at:
`hackathon/2022_GYBS/input/lightsheet/subject/subject0.zarr`
If you can register this file without the need to first down-sample it would be a huge boon! The
dataset contains a full resolution pyramid as well.

### Reading the datasets

Instructions for reading the datasets are provided here for python. I recommend using `nibabel`
and `zarr` packages.

Example working with the atlas:

```python
from pathlib import Path

import nibabel as nib

# loading the atlas nifti file
ATLAS_SOURCE = Path('lightsheet/reference/average_template_25_mm_half.nii.gz')
img = nib.load(ATLAS_SOURCE)
# indexing into the array is similar to numpy
new = img.slicer[0]
# If you want to save a nifti you can use this syntax
nib.save(new, ATLAS_SINK)
```

#### Example reading the challenge dataset nifti files in bulk:

```python
from pathlib import Path

import nibabel as nib

# set root path to folder containing nifti files
root = Path('lightsheet/subject/')
# get a list of all the challenge dataset nifti files
files = list(root.glob('subject*_25.nii.gz'))
# iterate over the files and read them
for f in files:
    img = nib.load(f)
    # indexing into the array is similar to numpy
    new = img.slicer[0]
```

#### Example reading the challenge dataset NGFF files in bulk:

```python
from pathlib import Path

import zarr

# set root path to folder containing nifti files
root = Path('lightsheet/subject/')
# get a list of all the challenge dataset nifti files
files = list(root.glob('subject*_25.zarr'))
# iterate over the files and read them
for f in files:
    # open the dataset
    dataset = zarr.open(f)
    # get full size image
    image = dataset['0']
    # copy the image to a numpy array 
    array = image[:]
    # the data has 5 dimensions (TCZYX). Lets squeeze out T and C since the have length 1 and 
    # just get a 3d Z,Y,X array.
    array = array.squeeze()
    
    # most of the relevant metadata can be found here. The metadata is stored as a json so you 
    # can also view it in a text editor. Just open `.zattrs` in the .zarr root directory. 
    meta = dataset.attrs['multiscales']

    # You can accesss lower resolution levels of the resolution pyramid like this. Parse the 
    # metadata to find out their resolution. 
    level_1 = dataset['1']
    level_2 = dataset['2']
```

#### Reading the full resolution dataset
Same flow as for NGFF files described above.

### Tips

- The atlas and data should already be in matching orientations and resolutions to allow you to
  focus on registration.
- The zarr files have 5 dimensions to mirror real world data (T,C,Z,Y,X). T and c are length 1. You
  can ignore them.
- The datasets are listed in roughly their difficulty to register. Later samples may have damage or
  be slightly rotated to make things interesting.
- The light-sheet image data may have slight shrinkage that needs accounting for.
