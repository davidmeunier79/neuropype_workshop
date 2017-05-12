""" Parameters file for run_power_analysis.py """

from params import *

data_type = 'fif'

# -------------------------- SET power variables --------------------------#
fmin = 0
fmax = 300
power_method = 'welch'
is_epoched = False

# workflow directory within the main_path dir
power_analysis_name = 'power_pipeline'

