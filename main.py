'''
STEPS : 
Use 'https://www.tunemymusic.com/transfer/spotify-to-file' to get csv from youtube/spotify playlist
Download CSV file local folder (myDB)
Install python 3.9+
Make a virtual env (python -m venv env)
Activate virtual env (VS code -> Select interpreter or env->Scripts->activate.bat)
Install required modules (pip install requirements.txt)
Run main.py
Logs file : (local path)/logs.log

Developer : Vaibhav Sharma
'''
from base.linker import download_vdo,download_by_search
from base.db_read import readData,readDBFolder
import logging

logging.basicConfig(filename="logs.log",format='%(asctime)s %(message)s',filemode='w',level=logging.INFO)
logger = logging.getLogger('main_script')

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

    download_start_index = 0 if download_start_index == '' else int(download_start_index)-1
    download_end_index = len(list_songs) if download_end_index == '' else int(download_end_index)
    
    for songX in list_songs[download_start_index:download_end_index]:
        download_by_search(songX,yourOutputFolder)


    
