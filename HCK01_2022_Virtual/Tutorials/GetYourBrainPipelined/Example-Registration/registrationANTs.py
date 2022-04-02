import ants
import sys
import os
import logging

iDir = os.getenv("INPUT_DIR")
oDir = os.getenv("OUTPUT_DIR")

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

if len(sys.argv) > 3:

    log.info("Starting ANTs registration")
    movingFile = os.path.join(iDir, sys.argv[1])
    fixedFile = os.path.join(iDir, sys.argv[2])
    warpedFile = os.path.join(oDir, sys.argv[3])


    log.info("Opening input")
    moving = ants.image_read(movingFile)
    fixed = ants.image_read(fixedFile)

    log.info("Run registration")
    mytx = ants.registration(fixed=fixed , moving=moving, type_of_transform='antsRegistrationSyNQuick[s]', verbose=True )
    log.info("Apply transforms")
    mywarpedimage = ants.apply_transforms(fixed=fixed, moving=moving, transformlist=mytx['fwdtransforms'])

    log.info("Save output")
    mywarpedimage.to_file(warpedFile)


log.info("Done ANTs")