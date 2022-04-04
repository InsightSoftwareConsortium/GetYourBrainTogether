#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: Workflow
inputs:
  movingImage:
    type: File

  fixedImage:
    type: File

outputs:
  warpedMovingImage:
    type: File
    outputSource: register/warpedImage

steps:
  smoothMoving:
    run: smoothANTS.cwl
    in:
      inputImage: movingImage
    out: [smoothedImage]

  smoothFixed:
    run: smoothANTS.cwl
    in:
      inputImage: fixedImage
    out: [smoothedImage]
  
  register:
    run: registrationANTs.cwl
    in:
      movingImage: smoothMoving/smoothedImage
      fixedImage: smoothFixed/smoothedImage
    out: [warpedImage]
