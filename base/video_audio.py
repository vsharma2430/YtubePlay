import moviepy.editor as mp
from pathlib import Path
from os import path,remove
import logging
from base.time_calc import calculate_time_logger

logger = logging.getLogger('main_script')
 
@calculate_time_logger
def convert_video_to_audio(video_file:str,delete_video:bool=False):
    logger.info("Converting video file")
    try:
        clip = mp.VideoFileClip(video_file)
        file_name = Path(video_file).resolve().stem + '.mp3'
        clip.audio.write_audiofile(path.dirname(video_file) + '\\' + file_name)

    except:
        logger.warning('Conversion failed')
   
    try:
        if(delete_video):
            remove(video_file)
    except:
        logger.warning('Deletion failed')