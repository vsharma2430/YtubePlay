import os
import logging

def define_logger():
    logging.basicConfig(filename="logs.log",format='%(asctime)s %(message)s',filemode='w',level=logging.INFO)
    return logging.getLogger('main_script')

def create_default_dir():
    if(not os.path.exists('database')):
        os.mkdir('database')
        
    if(not os.path.exists('downloads')):
        os.mkdir('downloads')