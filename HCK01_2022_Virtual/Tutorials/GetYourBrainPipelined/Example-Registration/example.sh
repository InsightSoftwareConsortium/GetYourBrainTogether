#!/bin/bash
python3 /opt/scripts/save_inputs.py
python3 /opt/scripts/smoothITK.py r16.nii.gz 3.0 r16_smooth_itk.nii.gz
python3 /opt/scripts/smoothSimpleITK.py r16.nii.gz 3.0 r16_smooth_sitk.nii.gz
python3 /opt/scripts/smoothANTs.py r16.nii.gz 3.0 r16_smooth_ants.nii.gz
python3 /opt/scripts/registrationANTs.py r16.nii.gz r64.nii.gz r16_warped_ants.nii.gz
python3 /opt/scripts/registrationSimpleITK.py r16.nii.gz r64.nii.gz r16_warped_sitk.nii.gz
#python3 /scripts/registrationElastix.py r16.nii.gz r64.nii.gz r16_warped_elastix.nii.gz