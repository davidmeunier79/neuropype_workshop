""" Parameters file for run_spectral_modularity.py"""

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

# pipeline directory within the main_path dir
spectral_analysis_name = 'spectral_connectivity_' + data_type + \
                            '_' + con_method
