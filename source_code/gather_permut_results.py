        
import numpy as np
import pandas as pd

import os,glob
    
from params_conn import freq_band_names

from neuropype_graph.gather.gather_permuts import gather_con_values
from neuropype_graph.gather.gather_permuts import compute_signif_permut_con_values

from params import main_path

from params_permuts import ref_labels_file,ref_coords_file,mean_spectral_permut_analysis_name
from params_permuts import nb_permuts,alpha

def gather_permut_con_values():
    
   
    labels = np.array([line.strip() for line in open(ref_labels_file)],dtype  = 'str')
    
    print labels
    
    res_path = os.path.join(main_path,mean_spectral_permut_analysis_name)
    
    #### coords
    coords = np.loadtxt(ref_coords_file)

    print "coords: ",
    print coords.shape

    #for freq_band_name in ['alpha']:
    for freq_band_name in freq_band_names:
        
        print freq_band_name
        
        df = gather_con_values(res_path, freq_band_name, nb_permuts, labels)
        
        print df
        
        compute_signif_permut_con_values(df, res_path, freq_band_name, alpha, labels, coords,diff_sess = False)
        
if __name__ =='__main__':
    
    #### gathering results
    gather_permut_con_values()
    
    
    
    