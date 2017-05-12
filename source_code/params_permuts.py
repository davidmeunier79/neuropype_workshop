""" Parameters file for run_mean_spectral_permuts.py """

from params import *
from params_conn import *

import os

nb_permuts = 100

#alpha = 1.0/float(nb_permuts)
alpha = 0.05

#mean_spectral_permut_analysis_name = spectral_analysis_name + "_permuts_" + str(nb_permuts)

#ref_labels_file = os.path.join(main_path,"correct_channel_names.txt")
#ref_coords_file = os.path.join(main_path,"correct_channel_coords.txt")

##### graph ####
mean_spectral_permut_analysis_name = spectral_analysis_name + "_rada_permuts_" + str(nb_permuts)

mean_radatools_optim = "WS tfrf 1"
mean_con_den = 0.1