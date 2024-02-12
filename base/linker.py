from pytube import YouTube
from base.ytubemp3downloader import YouTubeMp3
import logging
import os

logger = logging.getLogger('main_script')

def download_vdo(link:str,output_path:str):
	try:
		if(not os.path.exists(output_path)):
			os.mkdir(output_path)
	except:
		logger.warning('Output path restricted')

	try:
		yt = YouTube(link)
		logger.info('Downloading ' + yt.title)
		yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=output_path)
		logger.info('Download complete')
	except:
		logger.warning('Download failed')

def getLink(songName:str):
	youtube = YouTubeMp3()
	try:
		logger.info('Search started for ' + songName)
		result = youtube.find_video_link_by_name(songName)
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
		link = getLink(search_string)
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