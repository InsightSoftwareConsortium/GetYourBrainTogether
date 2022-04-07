# Adaptation of brainreg

## Developers

- Brainglobe (https://github.com/brainglobe) - @adamltyson and others
- Iana Vasylieva (adaptation of the existing package) @noisysky

## Registration Pipeline Description

Attempt to adapt an existing open-source package brainreg (https://github.com/brainglobe/brainreg) to the challenge dataset and BIL.
brainreg is a Python wrap for NiftyReg (http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg).

- Added pre-processing (stripes removal using FFT, background removal using mask)
- Added conversion from .nii.gz to tiff accepted by brainreg.
- Wrapped in Singularity container and a primitive CWL workflow

## Example Outcomes

link to the output: /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output
link to the Singularity image: /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg.sif

output contains:
transformed image - /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output/downsampled_standard.tiff
(or /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output/niftyreg/downsampled_standard.nii)
affine matrix - /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output/niftyreg/affine_matrix.txt
deformation field - /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output/niftyreg/deformation_field.nii
downsampled raw data file - /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output/niftyreg/downsampled.nii
atlas registered to original image - /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output/niftyreg/registered_atlas.nii
etc.


## Reproducibility

To reproduce results:
run the Singularity image
cd /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky
export SINGULARITY_BINDPATH="/bil/data/hackathon/2022_GYBS/input/fMOST/subject,/bil/data/hackathon/2022_GYBS/output/fMOST/noisysky"
./brainreg.sif -i /bil/data/hackathon/2022_GYBS/input/fMOST/subject/194061_red_mm_SLA.nii.gz -o /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output/ -v 10 10 10 --orientation sla

To run on new datasets, call with different
input file path (-i option),
output folder (-o option),
orientation (--orientation)
and voxel spacing (in the same order of axes as orientation) (-v option).


## Lessons Learned

brainreg is very well documented, therefore it was easy to understand how to use it. Most of other packages have very little to no examples/tutorials.
Pre-processing helps to improve the result.
Future improvements: CWL workflow

## Background and References

github repo: https://github.com/noisysky/GYBS_hackathon/
brainreg: https://github.com/brainglobe/brainreg
NiftyReg: https://sourceforge.net/projects/niftyreg/

Publications:
https://www.biorxiv.org/content/10.1101/2021.05.21.445133v1.full.pdf+html and references therein
