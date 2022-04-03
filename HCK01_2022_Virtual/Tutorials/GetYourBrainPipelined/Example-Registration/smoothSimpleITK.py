import SimpleITK as sitk
import sys
import os
import logging

iDir = os.getenv("INPUT_DIR")
oDir = os.getenv("OUTPUT_DIR")

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

if len(sys.argv) > 2:

    log.info("Starting SimpleITK")
    inFile = os.path.join(iDir, sys.argv[1])
    sigma = float(sys.argv[2])
    outFile = os.path.join(oDir, sys.argv[3])

    log.info("Reading inputs")
    reader = sitk.ImageFileReader()
    reader.SetFileName(inFile)
    image = reader.Execute()

    #pixelID = image.GetPixelID()

    log.info("Setup filter")
    gaussian = sitk.SmoothingRecursiveGaussianImageFilter()
    gaussian.SetSigma(float(sys.argv[2]))

    log.info("Run filter")
    image = gaussian.Execute(image)

    #caster = sitk.CastImageFilter()
    #caster.SetOutputPixelType(pixelID)
    #image = caster.Execute(image)

    log.info("Save output")
    writer = sitk.ImageFileWriter()
    writer.SetFileName(outFile)
    writer.Execute(image)
    
log.info("Done SimpleITK")