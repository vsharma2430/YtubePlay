from google_apis import create_service

class YouTube:
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube',
              'https://www.googleapis.com/auth/youtube.force-ssl']

    def __init__(self, client_file):
        self.service = None
        self.client_file = client_file
        
    def init_service(self):        
        self.service = create_service(self.client_file, self.API_NAME, self.API_VERSION, self.SCOPES)

    def my_playlists(self):
        playlists = []
        response = self.service.playlists().list(
            part='id,contentDetails,player,snippet,status',
            mine=True,
            maxResults=50
        ).execute()

        playlists.extend(response.get('items'))
        next_page_token = response.get('nextPageToken')

        while next_page_token:
            response = self.service.playlists().list(
                part='id,contentDetails,player,snippet,status',
                mine=True,
                maxResults=50,
                pageToken=next_page_token
            ).execute()            
            playlists.extend(response.get('items'))
            next_page_token = response.get('nextPageToken')
        return playlists 

    def create_playlist(self, title, description=None, privacy_status='public'):
        """
        visit https://developers.google.com/youtube/v3/docs/playlists#resource for
        request json representation and parameters
        """
        request_body = {
            'snippet': {
                'title': title,
                'description': description,
            },
            'status': {
                'privacyStatus': privacy_status
            }
        }
        response = self.service.playlists().insert(
            part='snippet,status',
            body=request_body
        ).execute()
        return response

    def update_playlist(self, playlist_id, title, description=None, privacy_status=None):
        request_body = {
            'id': playlist_id,
            'snippet': {
                'title': title,
                'description': description
            },
            'status': {
                'privacyStatus': privacy_status
            }
        }
        print(request_body)
        response = self.service.playlists().update(
            part='snippet,status',
            body=request_body
        ).execute()
        return response

    def delete_playlist(self, playlist_id):
        self.service.playlists().delete(id=playlist_id).execute()