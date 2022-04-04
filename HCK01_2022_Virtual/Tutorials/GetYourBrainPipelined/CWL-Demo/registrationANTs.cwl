#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: CommandLineTool


requirements:
  DockerRequirement:
    dockerPull: "example-reg"
    dockerOutputDirectory: /data/output
  SubworkflowFeatureRequirement: {}

baseCommand: ["python3", "/opt/scripts/registrationANTs.py"]
inputs:
  movingImage:
    type: File
    inputBinding:
      position: 1

  fixedImage:
    type: File
    inputBinding:
      position: 1
  
  warpedMovingImage:
    type: string
    inputBinding:
      position: 3
    default: movingWarped.nii.gz

outputs: 
  warpedImage:  
    type: File
    outputBinding:
      glob: $(inputs.warpedMovingImage)
