import ants
import sys
import os
import logging

iDir = os.getenv("INPUT_DIR")
oDir = os.getenv("OUTPUT_DIR")
name1 = os.path.join(iDir,"r16.nii.gz")
name2 = os.path.join(iDir,"r64.nii.gz")

if not os.path.exists(name1):
    fname1 = ants.get_ants_data('r16')
    i1 = ants.image_read(fname1)
    i1.to_file(name1)

if not os.path.exists(name2):
    fname2 = ants.get_ants_data('r64')
    i2 = ants.image_read(fname2)
    i2.to_file(name2)