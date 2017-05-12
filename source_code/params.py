
import getpass

if getpass.getuser() == 'david':
        
    main_path = '/mnt/Data/Omega/' ### David
    subject_ids = ['sub-0003']
elif getpass.getuser() == 'pasca':
  
    main_path = '/run/media/pasca/paska/meg_data/omega/sample_BIDS_omega/'  ### Annalisa
    subject_ids = ['sub-0003']
else:
    
    #TODO set here your data path!!!
    main_path = ''  
    subject_ids = ['sub-0003', 'sub-0004', 'sub-0006']

sessions = ['ses-0001']

data_path = main_path
