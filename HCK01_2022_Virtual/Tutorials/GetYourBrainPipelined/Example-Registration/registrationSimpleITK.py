#!/usr/bin/env python

# Example registration code from:
# https://simpleitk.readthedocs.io/en/master/link_ImageRegistrationMethodDisplacement1_docs.html


import SimpleITK as sitk
import sys
import os
import logging


def command_iteration(method):
    if (method.GetOptimizerIteration() == 0):
        print(f"\tLevel: {method.GetCurrentLevel()}")
        print(f"\tScales: {method.GetOptimizerScales()}")
    print(f"#{method.GetOptimizerIteration()}")
    print(f"\tMetric Value: {method.GetMetricValue():10.5f}")
    print(f"\tLearningRate: {method.GetOptimizerLearningRate():10.5f}")
    if (method.GetOptimizerConvergenceValue() != sys.float_info.max):
        print(f"\tConvergence Value: {method.GetOptimizerConvergenceValue():.5e}")


def command_multiresolution_iteration(method):
    print(f"\tStop Condition: {method.GetOptimizerStopConditionDescription()}")
    print("============= Resolution Change =============")


#if len(sys.argv) < 4:
#    print("Usage:", sys.argv[0], "<fixedImageFilter> <movingImageFile>", "<outputTransformFile>")
#    sys.exit(1)

iDir = os.getenv("INPUT_DIR")
oDir = os.getenv("OUTPUT_DIR")

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

if len(sys.argv) > 3:

    log.info("Starting SimpleITK registration")
    movingFile = os.path.join(iDir, sys.argv[1])
    fixedFile = os.path.join(iDir, sys.argv[2])
    warpedFile = os.path.join(oDir, sys.argv[3])


    log.info("Load inputs")
    fixed = sitk.ReadImage(fixedFile, sitk.sitkFloat32)
    moving = sitk.ReadImage(movingFile, sitk.sitkFloat32)

    initialTx = sitk.CenteredTransformInitializer(fixed, moving, sitk.AffineTransform(fixed.GetDimension()))

    R = sitk.ImageRegistrationMethod()

    R.SetShrinkFactorsPerLevel([3, 2, 1])
    R.SetSmoothingSigmasPerLevel([2, 1, 1])

    R.SetMetricAsJointHistogramMutualInformation(20)
    R.MetricUseFixedImageGradientFilterOff()

    R.SetOptimizerAsGradientDescent(learningRate=1.0,numberOfIterations=100,estimateLearningRate=R.EachIteration)
    R.SetOptimizerScalesFromPhysicalShift()

    R.SetInitialTransform(initialTx)

    R.SetInterpolator(sitk.sitkLinear)

    #R.AddCommand(sitk.sitkIterationEvent, lambda: command_iteration(R))
    #R.AddCommand(sitk.sitkMultiResolutionIterationEvent,lambda: command_multiresolution_iteration(R))

    log.info("Start registration")
    outTx1 = R.Execute(fixed, moving)

    #print("-------")
    #print(outTx1)
    #print(f"Optimizer stop condition: {R.GetOptimizerStopConditionDescription()}")
    #print(f" Iteration: {R.GetOptimizerIteration()}")
    #print(f" Metric value: {R.GetMetricValue()}")

    displacementField = sitk.Image(fixed.GetSize(), sitk.sitkVectorFloat64)
    displacementField.CopyInformation(fixed)
    displacementTx = sitk.DisplacementFieldTransform(displacementField)
    del displacementField
    displacementTx.SetSmoothingGaussianOnUpdate(varianceForUpdateField=0.0,varianceForTotalField=1.5)

    R.SetMovingInitialTransform(outTx1)
    R.SetInitialTransform(displacementTx, inPlace=True)

    R.SetMetricAsANTSNeighborhoodCorrelation(4)
    R.MetricUseFixedImageGradientFilterOff()

    R.SetShrinkFactorsPerLevel([3, 2, 1])
    R.SetSmoothingSigmasPerLevel([2, 1, 1])

    R.SetOptimizerScalesFromPhysicalShift()
    R.SetOptimizerAsGradientDescent(learningRate=1,numberOfIterations=300,estimateLearningRate=R.EachIteration)

    R.Execute(fixed, moving)

    #print("-------")
    #print(displacementTx)
    #print(f"Optimizer stop condition: {R.GetOptimizerStopConditionDescription()}")
    #print(f" Iteration: {R.GetOptimizerIteration()}")
    #print(f" Metric value: {R.GetMetricValue()}")

    compositeTx = sitk.CompositeTransform([outTx1, displacementTx])
    #sitk.WriteTransform(compositeTx, sys.argv[3])

    if ("SITK_NOSHOW" not in os.environ):
        #sitk.Show(displacementTx.GetDisplacementField(), "Displacement Field")

        resampler = sitk.ResampleImageFilter()
        resampler.SetReferenceImage(fixed)
        resampler.SetInterpolator(sitk.sitkLinear)
        resampler.SetDefaultPixelValue(0)
        resampler.SetTransform(compositeTx)

        out = resampler.Execute(moving)
        
        writer = sitk.ImageFileWriter()
        writer.SetFileName(warpedFile)
        writer.Execute(out)
        

        simg1 = sitk.Cast(sitk.RescaleIntensity(fixed), sitk.sitkUInt8)
        simg2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)
        cimg = sitk.Compose(simg1, simg2, simg1 // 2. + simg2 // 2.)
        #sitk.Show(cimg, "ImageRegistration1 Composition")