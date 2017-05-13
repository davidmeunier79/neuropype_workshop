# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:44:00 2015

@author: pasca
"""
import os
import getpass

is_nii = True  # True if you have MRI files in nii format

if getpass.getuser() == 'pasca':
    main_path = '/run/media/pasca/paska/meg_data/omega/sample_BIDS_omega/'
    sbj_dir = os.path.join(main_path, 'FSF')
    MRI_path = main_path
    subjects_list = ['sub-0002'] 

elif getpass.getuser() == 'karim':
    main_path = '/media/karim/DATA/omega/sample_BIDS_omega'
    sbj_dir = os.path.join(main_path, 'FSF')
    MRI_path = main_path
    subjects_list = ['sub-0004', 'sub-0006']

else:
    main_path = ''           # data dir
    subjects_list = ['sub-0003']

# dir names in main_path=sbj_dir
FS_WF_name = "segmentation_workflow"
BEM_WF_name = "watershed_bem"
MAIN_WF_name = "main_workflow"
