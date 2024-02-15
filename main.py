'''
STEPS : 
README.md for steps

Developer : Vaibhav Sharma
'''
from base.linker import download_vdo,download_by_search
from base.db_read import readData,readDBFolder
from base.time_calc import calculate_time
import logging
from concurrent import futures

logging.basicConfig(filename="logs.log",format='%(asctime)s %(message)s',filemode='w',level=logging.INFO)
logger = logging.getLogger('main_script')

def thread_helper(args):
    download_by_search(args[0],args[1])

@calculate_time
def generate_download_threads(num, values,output_path):
    args = ((value, output_path) for value in values)
    with futures.ThreadPoolExecutor(num) as tex:
        for _ in tex.map(thread_helper,args):
            pass

if __name__ == "__main__":

    yourDB :str  = input('Enter DB file/folder Location ? (default : myDB)') 
    yourOutputFolder :str = input('Enter output Location ? (default : downloads)')

    yourDB = 'myDB' if yourDB == '' else yourDB
    yourOutputFolder = 'downloads' if yourOutputFolder == '' else yourOutputFolder

    list_songs = readData(yourDB) if '.' in yourDB else readDBFolder(yourDB)
    song_index = 1
    for songX in list_songs : 
        print(str(song_index) + '. ' + songX)
        song_index = song_index + 1

    download_start_index = input('Download start index ? (default : 1)')
    download_end_index = input('Download end index ? (default : '+ str(len(list_songs)) + ')')
    simultaneous_downloads = input('Simulatneous downloads ? (default : 25)')

    download_start_index = 0 if download_start_index == '' else int(download_start_index)-1
    download_end_index = len(list_songs) if download_end_index == '' else int(download_end_index)
    simultaneous_downloads = 10 if download_end_index == '' else int(simultaneous_downloads)
    
    current_index = 1
    download_song_list = list_songs[download_start_index:download_end_index]
    
    print('Total songs : ' + str(len(download_song_list)))
    generate_download_threads(simultaneous_downloads,download_song_list,yourOutputFolder)
    
    '''
    single thread code  
       for songX in list_songs[download_start_index:download_end_index]:
        download_by_search(songX,yourOutputFolder)
        print('Complete : ' + str(current_index)  + ' of ' + str(len(download_song_list)))
        current_index = current_index + 1
    '''

    




    
