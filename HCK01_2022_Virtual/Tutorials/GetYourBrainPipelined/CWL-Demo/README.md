# GetYourBrainPipelined - CWL Demo
Demo of a simple Common Workflow Language (CWL) pipeline to smooth two images and then do a simple registration

# Prerequisites
Make sure you have ran through the containers demo (see '../Containers.md'). Specifically, you will need the following files generated from the demo:

- Built singularity container file: 
```
example-reg.sif
```
- Input test image files: 
```
data_input/r16.nii.gz
data_input/r64.nii.gz
```

Your will also have to install CWL on BIL by running:

```
module load anaconda3/4.11.0
pip install --user cwltool cwlref-runner

```


# Demo Steps:
1. Move the contents of this directory into the same directory as the 'example-reg.sif'
2. Edit 'exampleRegInputs.yml' to match your local path for the test images (this is an example input definition to send through the pipeline)
3. To call the demo pipelin on BIL, run the following command:

```
 cwl-runner --singularity examplePipeline.cwl exampleRegInputs.yml

```
