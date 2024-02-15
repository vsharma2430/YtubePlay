from pytube import YouTube
from base.ytubemp3downloader import YouTubeMp3
from base.video_audio import convert_video_to_audio
from os import path,mkdir
from base.time_calc import calculate_time_logger
import logging

logger = logging.getLogger('main_script')

@calculate_time_logger
def download_vdo(link:str,output_path:str,format:int=2):
	'''
	format - 1 : video
	format - 2 : audio
	'''
	try:
		if(not path.exists(output_path)):
			mkdir(output_path)
	except:
		logger.warning('Output path restricted')

	try:
		yt = YouTube(link)
		logger.info('Downloading ' + yt.title)
		saved_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=output_path)
		logger.info('Download complete')
		if (format == 2) :
			convert_video_to_audio(saved_video,False)

	except:
		logger.warning('Download failed')

def get_link(song_name:str):
	youtube = YouTubeMp3()
	try:
		logger.info('Search started for ' + song_name)
		result = youtube.find_video_link_by_name(song_name)
		link = result[1]
		title = result[0]['title']
	except:
		logger.warning('Song search failed')
		pass
	else:
		logger.info(f"Song Found: '{title}'")
		return link

def download_by_search(search_string:str,download_path:str=''):
	try:
		print('Download by search operation started for ' + search_string)
		link = get_link(search_string.strip())
		download_vdo(link,download_path)
		print('Download by search operation complete for ' + search_string)
	except:
		pass

def getLinks(file:str,songs:list) -> list:
	global youtube
	global path

	file = file.replace("\\","/")
	path = f"./{file.split('.')[0].split('/')[-1]}_Musics"

	youtube = YouTubeMp3(path=path)

	links = []
	links.append('Song Name,Link')

	for song in songs:
		try:
			result = youtube.find_video_link_by_name(song)
			link = result[1]
			title = result[0]['title']
			links.append(song.replace(',',';') + ',' +  link)
		except:
			pass
		else:
			logger.info(f"Song Found: '{title}'")

	logger.info(f"\n{len(links)} Songs Found.\n")
	return links