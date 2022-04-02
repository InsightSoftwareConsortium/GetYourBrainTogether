import ants
import sys
import os
import logging

iDir = os.getenv("INPUT_DIR")
oDir = os.getenv("OUTPUT_DIR")

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

if len(sys.argv) > 2:

    log.info("Starting")
    inFile = os.path.join(iDir, sys.argv[1])
    sigma = float(sys.argv[2])
    outFile = os.path.join(oDir, sys.argv[3])

    log.info("Opening input")
    im = ants.image_read(inFile)

    log.info("Setup/Run filter")
    outIm = ants.utils.smooth_image(im, sigma)

    log.info("Save output")
    outIm.to_file(outFile)


log.info("Done ANTs")