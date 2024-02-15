import os
from base.thread import generate_download_threads
from base.db_read import readDir
from base.console_rw import user_input,get_int,print_console
from base.time_calc import get_date_stamp

def csv_download_routine_advanced():
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

def csv_download_routine_simple():
    database : str = 'database'
    if(not os.path.isdir(database) and not os.path.exists(database)):
        database :str  = user_input('Enter DB file/folder Location ?', 'database') 
    list_songs = readDir(database) 
    download_start_index = 0
    download_end_index = len(list_songs)
    download_location :str = 'downloads_' + get_date_stamp()
    simultaneous_download_thread_count = 25
    download_song_list = list_songs[download_start_index:download_end_index]
    
    print('Total songs : ' + str(len(download_song_list)))
    generate_download_threads(simultaneous_download_thread_count,download_song_list,download_location)