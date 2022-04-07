# Adaptation of brainreg

## Developers

- Brainglobe (https://github.com/brainglobe) - @adamltyson and others
- Iana Vasylieva (adaptation of the existing package) @noisysky

## Registration Pipeline Description

Attempt to adapt an existing open-source package `brainreg` (https://github.com/brainglobe/brainreg) to the challenge dataset and BIL.<br/>
`brainreg` is a Python wrap for NiftyReg (http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg).

- Added pre-processing (stripes removal using FFT, background removal using mask)
- Added conversion from .nii.gz to tiff accepted by brainreg.
- Wrapped in Singularity container

## Example Outcomes

Transformed fMOST image:
![alt text](https://github.com/InsightSoftwareConsortium/GetYourBrainStraight/blob/main/HCK01_2022_Virtual/ReproducibleResource/IanaVasylieva/fMOST_transformed.png)

Atlas registered to original fMOST image:
![alt text](https://github.com/InsightSoftwareConsortium/GetYourBrainStraight/blob/main/HCK01_2022_Virtual/ReproducibleResource/IanaVasylieva/fMOST_brainreg.png)

**path to the output**: /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output<br/>
**path to the Singularity image**: /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg.sif<br/>

output contains:<br/>
**transformed image** - /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output/downsampled_standard.tiff
(or /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output/niftyreg/downsampled_standard.nii)<br/>
**affine matrix** - /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output/niftyreg/affine_matrix.txt<br/>
**deformation field** - /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output/niftyreg/deformation_field.nii<br/>
**downsampled raw data file** - /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output/niftyreg/downsampled.nii<br/>
**atlas registered to original image** - /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output/niftyreg/registered_atlas.nii<br/>
etc.


## Reproducibility

To reproduce results:<br/>
<br/>
run cwl workflow:<br/><br/>
`load module anaconda3`<br/>
`pip install --user cwltool cwlref-runner`<br/>
`cd /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky`<br/>
`cwltool brainreg.cwl message.yml`<br/>
<br/>
or<br/>
run the Singularity image directly<br/><br/>
`cd /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky`<br/>
`export SINGULARITY_BINDPATH="/bil/data/hackathon/2022_GYBS/input/fMOST/subject,/bil/data/hackathon/2022_GYBS/output/fMOST/noisysky"`<br/>
`./brainreg.sif -i /bil/data/hackathon/2022_GYBS/input/fMOST/subject/194061_red_mm_SLA.nii.gz -o /bil/data/hackathon/2022_GYBS/output/fMOST/noisysky/brainreg_output/ -v 10 10 10 --orientation sla`<br/>

To run on new datasets, call with different<br/>
input file path (-i option),<br/>
output folder (-o option),<br/>
orientation (--orientation)<br/>
and voxel spacing (in the same order of axes as orientation) (-v option).


## Lessons Learned

- brainreg is very well documented (https://docs.brainglobe.info/brainreg/tutorial), therefore it was easy to understand how to use it. Most of other packages have very little to no examples/tutorials.<br/>
- Pre-processing helps to improve the result.<br/>
- Future improvements: more advanced CWL workflow

## Background and References

github repo: https://github.com/noisysky/GYBS_hackathon/<br/>
brainreg: https://github.com/brainglobe/brainreg<br/>
NiftyReg: https://sourceforge.net/projects/niftyreg/<br/>

Publications:
https://www.biorxiv.org/content/10.1101/2021.05.21.445133v1.full.pdf+html and references therein
