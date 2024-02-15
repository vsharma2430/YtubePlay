'''
STEPS : 
README.md for steps

Developer : Vaibhav Sharma
'''
from base.console_rw import user_input,get_int
from base.csv_download import csv_download_routine_simple,csv_download_routine_advanced
from base.search_download import search_download_routine
from base.link_download import link_download_routine
from base.default import define_logger,create_default_dir

if __name__ == "__main__":
    logger = define_logger()
    create_default_dir()
    
    download_type : int = 1
    while(download_type < 5):
        print('Welcome to YtubePlay')
        download_type = get_int(user_input('Choose download type : 1.Title 2.Link 3.CSV(simple) 4.CSV(Advanced) 5.Exit','1'),1)
        if(download_type == 1):
            search_download_routine()
        elif(download_type == 2):
            link_download_routine()
        elif(download_type == 3):
            csv_download_routine_simple()
        elif(download_type == 4):
            csv_download_routine_advanced()
        else:
            break
        print('Operation complete\n')
    
    feedback = user_input('Thanks you.\nPress enter to exit')
    
    




    
