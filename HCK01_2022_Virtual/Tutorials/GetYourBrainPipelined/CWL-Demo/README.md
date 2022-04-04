# GetYourBrainPipelined
Demo of a simple CWL pipeline to smooth two images and then do a simple registration

# Prerequisites
Make sure you have ran through the containers demo (see '../containers.md'). Specifically, we will need the following files generated from the previous demo:

Built singularity container image: 'example-reg.sif'
Input files: 'data_input/r16.nii.gz' and 'data_input/r64.nii.gz'

Your will also have to install cwl. On BIL you can do this by running:

```
module load anaconda3/4.11.0
pip install --user cwltool cwlref-runner

```


# Demo Steps:
1.) Move the contents of this directory into the same directory as the 'example-reg.sif'
2.) Edit 'exampleRegInputs.yml' to match your local path for the images (this is an example input to send through the pipeline)

4.) To call the demo pipeline on BIL, run the following command:

```
 cwl-runner --singularity examplePipeline.cwl exampleRegInputs.yml

```
