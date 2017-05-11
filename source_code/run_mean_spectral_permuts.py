# -*- coding: utf-8 -*-


"""
Compute mean correlation matrices and possibly compute graph analysis over 
"""
#import sys, os

import nipype as pe
import nipype.interfaces.utility as niu
import nipype.interfaces.io as nio

from params_permuts import nb_permuts,ref_labels_file,ref_coords_file,freq_band_names

from params_permuts import main_path,spectral_analysis_name,mean_spectral_permut_analysis_name

#from define_variables import ROI_coords_file,ROI_MNI_coords_file,ROI_labels_file 

from neuropype_graph.nodes.correl_mat import PrepareMeanCorrel
#from neuropype_graph.pipelines.conmat_to_graph import create_pipeline_conmat_to_graph_density

from neuropype_graph.nodes.graph_stats import ShuffleMatrix

#from dmgraphanalysis.coclass import *
    
######################################### Infosources
    
def create_infosource():
    
    infosource = pe.Node(interface=niu.IdentityInterface(fields=['seed','freq_band']),name="infosource")
    
    infosource.iterables = [('freq_band',freq_band_names),('seed',range(-1,nb_permuts))]
    return infosource


######################################### Datasources
    
def create_datasource_correl():

    datasource = pe.Node(interface=nio.DataGrabber(infields = ['freq_band'],outfields=['Z_cor_mat_files','coords_files']),name = 'datasource')
    
    datasource.inputs.base_directory = main_path
    
    datasource.inputs.template = '%s/%s/_freq_band_name_%s_sess_index_*_subject_id_*/%s/%s%s'
    
    datasource.inputs.template_args = dict(
    #Z_cor_mat_files=[[cor_mat_analysis_name,"nii_to_conmat","compute_conf_cor_mat","Z_cor_mat_resid_ts",".npy"]],
    coords_files= [[spectral_analysis_name,"",'freq_band', "create_ts","correct_channel_coords",".txt"]])
    #labels_files= [[spectral_analysis_name,"",'freq_band', "create_ts","correct_channel_names",".txt"]])
    Z_cor_mat_files=[[spectral_analysis_name,"ts_to_conmat",'freq_band',"spectral","conmat_0_coh",".npy"]],
    
    datasource.inputs.sort_filelist = True
    
    return datasource

######################################### Full analysis
    
def run_mean_correl():
    
    main_workflow = pe.Workflow(name= mean_spectral_permut_analysis_name)
    main_workflow.base_dir = main_path
    
    #### infosource 
    
    infosource = create_infosource()
        
    #### Data source
    #datasource = create_datasource_rada_by_reg_memory_signif_conf()
    datasource = create_datasource_correl()
            
    main_workflow.connect(infosource,'freq_band',datasource,'freq_band')
        
        
        
        
    #### prepare_mean_correl
    prepare_mean_correl = pe.Node(interface = PrepareMeanCorrel(), name='prepare_mean_correl')
    
    prepare_mean_correl.inputs.gm_mask_coords_file = ref_coords_file
    #prepare_mean_correl.inputs.labels_file = ref_labels_file
     
    main_workflow.connect(datasource, 'Z_cor_mat_files',prepare_mean_correl,'cor_mat_files')
    #main_workflow.connect(datasource, 'labels_files',prepare_mean_correl,'labels_files')
    main_workflow.connect(datasource, 'coords_files',prepare_mean_correl,'coords_files')
    
    
    ### shuffle matrix
    shuffle_matrix = pe.Node(interface = ShuffleMatrix(), name='shuffle_matrix')
    
    main_workflow.connect(prepare_mean_correl, 'avg_cor_mat_matrix_file',shuffle_matrix,'original_matrix_file')
    main_workflow.connect(infosource, 'seed',shuffle_matrix,'seed')
    
    ################################################ modular decomposition on norm_coclass ############################################
	
    #if 'rada' in mean_correl_permut_analysis_name.split('_'):
        
        #graph_den_pipe = create_pipeline_conmat_to_graph_density(pipeline_name = "graph_den_pipe",main_path = main_path, multi= False, con_den = mean_con_den,mod = True, plot = False, optim_seq = mean_radatools_optim)
        ##graph_den_pipe = create_pipeline_conmat_to_graph_density("graph_den_pipe",main_path,multi = False, con_den = con_den)
        
        #main_workflow.connect(shuffle_matrix,'shuffled_matrix_file',graph_den_pipe,'inputnode.conmat_file')
        
        #graph_den_pipe.inputs.inputnode.labels_file = ROI_labels_file
        #graph_den_pipe.inputs.inputnode.coords_file = ROI_MNI_coords_file
        
    
    
    
    
    return main_workflow
    
if __name__ =='__main__':
    
    main_workflow = run_mean_correl()
    
    
    #### Run workflow 
    main_workflow.config['execution'] = {'remove_unnecessary_outputs':'false'}
    
    main_workflow.run()
    #main_workflow.run(plugin='MultiProc', plugin_args={'n_procs' : 4})
