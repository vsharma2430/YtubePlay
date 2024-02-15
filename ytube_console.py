'''
STEPS : 
README.md for steps

Developer : Vaibhav Sharma
'''
from base.thread import generate_download_threads
from base.db_read import readDir
from base.console_rw import user_input,get_int,print_console
import logging

def define_logger():
    logging.basicConfig(filename="logs.log",format='%(asctime)s %(message)s',filemode='w',level=logging.INFO)
    logger = logging.getLogger('main_script')

if __name__ == "__main__":
    define_logger()
    database :str  = user_input('Enter DB file/folder Location ?', 'database') 
    list_songs = readDir(database) 
    print_console(list_songs)
    download_start_index = get_int(user_input('Download start index ?','1'),1)-1
    download_end_index = get_int(user_input('Download end index ?',str(len(list_songs))),len(list_songs))
    download_location :str = user_input('Enter output Location ?','downloads')
    simultaneous_download_thread_count = get_int(user_input('Simulatneous downloads ?','25'),25)
    download_song_list = list_songs[download_start_index:download_end_index]
    
    print('Total songs : ' + str(len(download_song_list)))
    generate_download_threads(simultaneous_download_thread_count,download_song_list,download_location)
    feedback = user_input('Thanks for using this application.')
    
    




    
