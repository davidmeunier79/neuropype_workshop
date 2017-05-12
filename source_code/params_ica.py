""" Parameters file for run_preprocess_pipeline.py """

from params import *

data_type = 'ds'

down_sfreq = 800
l_freq = 0.1
h_freq = 150


# ------------------------ SET ICA variables -----------------------------#

is_ICA = True  # True if we apply ICA to remove ECG and EoG artifacts

# specify ECG and EoG channel names if we know them
ECG_ch_name = 'ECG'
EoG_ch_name = 'HEOG, VEOG'
variance = 0.95

reject = dict(mag=5e-12, grad=5000e-13)

# workflow directory within the main_path dir
preproc_pipeline_name = 'preprocessing_pipeline'
