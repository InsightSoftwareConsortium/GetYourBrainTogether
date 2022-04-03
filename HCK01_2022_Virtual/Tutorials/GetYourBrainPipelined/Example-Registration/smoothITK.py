import itk
import sys
import os
import logging

iDir = os.getenv("INPUT_DIR")
oDir = os.getenv("OUTPUT_DIR")

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

if len(sys.argv) > 2:

    log.info("Starting ITK")
    inFile = os.path.join(iDir, sys.argv[1])
    sigma = float(sys.argv[2])
    outFile = os.path.join(oDir, sys.argv[3])

    log.info("Opening input")
    im = itk.imread(inFile)

    log.info("Setup filter")
    filter = itk.SmoothingRecursiveGaussianImageFilter[type(im), type(im)].New()
    filter.SetInput(im)
    filter.SetSigma(sigma)

    log.info("Run filter")
    filter.Update()
    outIm = filter.GetOutput()

    log.info("Save output")
    itk.imwrite(outIm, outFile)


log.info("Done ITK")