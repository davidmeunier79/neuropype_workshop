        
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
        

def gather_permut_rada_values():
    
    import numpy as np
    import pandas as pd
    
    import os,glob
    
    from neuropype_graph.gather.gather_permuts import compute_signif_permuts,compute_rada_df
    

    res_path = os.path.join(main_path,mean_correl_permut_analysis_name)

    xls_filename = os.path.join(res_path,"permuts_den_" + str(mean_con_den).replace(".","_")  + '_all_infos_by_sorted_cond.xls')
    
    if os.path.exists(xls_filename):
        
        df = pd.read_excel(xls_filename)
        
    else:
            
        all_global_info_values = []
        
        for seed in range(-1,nb_permuts):
        
            dict_global_info_values = {'Regressor':reg_name, 'Seed':seed}
            
            local_dir = os.path.join(res_path,"graph_den_pipe_den_" +str(mean_con_den).replace('.','_'),"_reg_" + reg_name + "_seed_" + str(seed))
            
            print local_dir
            
            compute_rada_df(iter_path = local_dir, df = dict_global_info_values)
                
            print dict_global_info_values
            
            all_global_info_values.append(dict_global_info_values)
                
        print all_global_info_values
        
        df = pd.DataFrame(all_global_info_values)
        
        list_cols = df.columns.tolist()
        
        list_cols.remove('Seed')
        list_cols.remove('Regressor')
        
        new_seq_col = ['Seed','Regressor'] + list_cols
        
        #csv_filename = os.path.join(res_path,"permuts_den_" + str(mean_con_den).replace(".","_") + "_" + ".".join(cond) + '_all_infos_by_sorted_cond_tmp.csv')
        
        #df.to_csv(csv_filename,columns = new_seq_col)
        
        df.to_excel(xls_filename,columns = new_seq_col)
        
    
    print df

    df_res = compute_signif_permuts(df, permut_col = "Seed", session_col = "Regressor", start_col = 0)
    
    xls_filename = os.path.join(res_path,"permuts_den_" + str(mean_con_den).replace(".","_") + "_" + reg_name +'_signif_by_sorted_cond.xls')

    df_res.to_excel(xls_filename)

if __name__ =='__main__':
    
    #### gathering results
    gather_permut_con_values()
    
    ### gathering rada values
    gather_permut_rada_values()
    
    
    
    