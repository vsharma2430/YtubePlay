from base.console_rw import user_input,get_int,print_console
from base.thread import generate_download_threads

def search_download_routine():
    song_names :str  = user_input('Enter song name(s) ?', 'Grew up at midnight') 
    download_location :str = user_input('Enter output Location ?','downloads')
    generate_download_threads(25,song_names.split(','),download_location)