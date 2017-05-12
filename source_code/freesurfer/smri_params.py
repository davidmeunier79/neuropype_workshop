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
    subjects_list = ['sub-0002']  # ['dmn_mri','Monk1'] ['monk0002']  'dmn_mri'

else:
    main_path = '/home/karim/Documents/Fanny'           # data dir
#    main_path = '/home/karim/Documents/Blindsight'  # data dir
    sbj_dir = os.path.join(main_path, "FSF")        # where FS creates sbj dir
    MRI_path = os.path.join(main_path, "MRI")       # MRI dir


    '''
    subjects_list = ["balai",'benba','casla','doble','droco','duple',
                     'frapa','haimo','laupa','levma','mahan','marle',
                     'merly','mesma','moryv','ricro','rimso','rougw',
                     'sanga','torgu','vanso','virje']

    subjects_list = ['monk0003','monk0004','monk0004','monk0005',
                     'monk0006','monk0007','monk0008','monk0009',
                     'monk0010','monk0011','monk0012']
    subjects_list = ['S02','S03', "S04",'S05','S06', "S07",'S08','S09',
                     "S10",'S11','S12', "S13",'S14','S15', "S16"]
    '''
#        subjects_list = ['sbj_1']
    subjects_list = ['sub-0002']

# dir names in main_path=sbj_dir
FS_WF_name = "segmentation_workflow"
BEM_WF_name = "watershed_bem"
MAIN_WF_name = "main_workflow"
