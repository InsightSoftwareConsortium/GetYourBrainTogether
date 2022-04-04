#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: CommandLineTool


requirements:
  DockerRequirement:
    dockerPull: "example-reg"
    dockerOutputDirectory: /data/output
  SubworkflowFeatureRequirement: {}

baseCommand: ["python3", "/opt/scripts/smoothANTs.py"]
inputs:
  inputImage:
    type: File
    inputBinding:
      position: 1

  smoothing:
    type: double
    inputBinding:
      position: 2
    default: 3.0  
  
  outputImage:
    type: string
    inputBinding:
      position: 3
    default: input_smoothed.nii.gz

outputs: 
  smoothedImage:  
    type: File
    outputBinding:
      glob: $(inputs.outputImage)
