""" Parameters file for run_spectral_modularity.py"""
import os

from params import *

data_type = 'fif'

# ----------------------- SET connectivity variables ----------------------#

# freq_bands = [[2, 4], [5, 7], [8, 12], [13, 29], [30, 59], [60, 90]]
# freq_band_names = ['delta', 'theta', 'alpha', 'beta', 'gamma1', 'gamma2']

freq_bands = [[8, 12], [13, 29]]
freq_band_names = ['alpha', 'beta']

# 'pli', 'plv', 'pli2_unbiased', 'coh', 'cohy', 'ppc', 'wpli'
# 'imcoh', 'wpli2_debiased', 'correl'
con_method = 'coh'
epoch_window_length = 3.0

## pipeline directory within the main_path dir
#spectral_analysis_name = 'spectral_connectivity_' + data_type + \
                            #'_' + con_method
                        
################################## graph 
con_den = 0.1
radatools_optim = "WS tfrf 1"

### for representation
ref_labels_file = os.path.join(main_path,"correct_channel_names.txt")
ref_coords_file = os.path.join(main_path,"correct_channel_coords.txt")


# pipeline directory within the main_path dir
spectral_analysis_name = 'spectral_connectivity_rada_' + data_type + \
                            '_' + con_method