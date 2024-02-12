from youtube import YouTube

client_file = 'client-secret.json'
yt = YouTube(client_file)
yt.init_service()

response_playlist = yt.create_playlist('<playlist title>', '<playlist description>', '<privacy status')
playlist_id = response_playlist.get('id')
playlist_title = response_playlist['snippet']['title']

video_ids = ['<video id1', '<video id2>', '<video id3>']
for video_id in video_ids:
    request_body = {
        'snippet': {
            'playlistId': playlist_id,
            'resourceId': {
                'kind': 'youtube#video',
                'videoId': video_id
            }
        }
    }
    response = yt.service.playlistItems().insert(
        part='snippet',
        body=request_body
    ).execute()
    video_title = response['snippet']['title']
    print(f'Video "{video_title}" inserted to {playlist_title} playlist')