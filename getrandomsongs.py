import os, random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotifycredentials import set_credentials

set_credentials()

spotipy_client_id = os.environ.get('SPOTIPY_CLIENT_ID')
spotipy_client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
spotipy_redirect_uri = os.environ.get('SPOTIPY_REDIRECT_URI')

scope = "user-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def getrandomurl(input,hipster=False):
	query_string = input + "%"
	if hipster:
		query_string += ' tag:hipster'
	results = sp.search(q=query_string,limit=50,type='album')
	album = random.choice(results['albums']['items'])
	song = random.choice(sp.album_tracks(album['external_urls']['spotify'])['items'])
	print(song['external_urls']['spotify'])

characters = [x for x in '0123456789abcdefghijklmnopqrstuvwxyz']
for x in range(100):
	getrandomurl(random.choice(characters),hipster=True)