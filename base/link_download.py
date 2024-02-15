from base.console_rw import user_input,get_int,print_console
from base.linker import download_vdo

def link_download_routine():
    link :str  = user_input('Enter song link(s) ?', r'https://www.youtube.com/watch?v=B3JcHWCA-VA') 
    download_location :str = user_input('Enter output Location ?','downloads')
    download_vdo(link=link,output_path=download_location)