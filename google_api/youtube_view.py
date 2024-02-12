from youtube import YouTube

client_file = 'client-secret.json'
yt = YouTube(client_file)
yt.init_service()

print(yt.my_playlists())