import itk
import sys
import os
import logging

iDir = os.getenv("INPUT_DIR")
oDir = os.getenv("OUTPUT_DIR")

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

if len(sys.argv) > 3:

    log.info("Starting Elastix registration")
    movingFile = os.path.join(iDir, sys.argv[1])
    fixedFile = os.path.join(iDir, sys.argv[2])
    warpedFile = os.path.join(oDir, sys.argv[3])


    log.info("Opening input")
    fixed = itk.imread(fixedFile)
    moving = itk.imread(movingFile)

    # Import Default Parameter Map
    parameter_object = itk.ParameterObject.New()
    parameter_map_rigid = parameter_object.GetDefaultParameterMap('rigid')
    parameter_map_bspline = parameter_object.GetDefaultParameterMap('bspline')

    parameter_object.AddParameterMap(parameter_map_rigid)
    parameter_object.AddParameterMap(parameter_map_bspline)

    log.info("Run registration")
    registered_image, params = itk.elastix_registration_method(fixed, moving, parameter_object=parameter_object,)

    log.info("Save output")
    itk.imwrite(registered_image, warpedFile)


log.info("Done Elastix")