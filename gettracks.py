import os, sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotifycredentials import set_credentials

set_credentials()

spotipy_client_id = os.environ.get('SPOTIPY_CLIENT_ID')
spotipy_client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
spotipy_redirect_uri = os.environ.get('SPOTIPY_REDIRECT_URI')

scope = "user-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def constructquery(album,track,artist,year,upc,hipster,new,isrc,genre):
	for key,value in locals().items():
		if value:
			yield f"{key}:{value}"

def makequery(album=None,track=None,artist=None,year=None,upc=None,hipster=None,new=None,isrc=None,genre=None):
	return ' '.join([x for x in constructquery(*locals().values())])

def geturl(album=None,track=None,artist=None,year=None,upc=None,hipster=None,new=None,isrc=None,genre=None):
	query_string = makequery(*locals().values())
	results = sp.search(q=query_string,limit=1,type='track')
	return results['tracks']['items'][0]['external_urls']['spotify']

def geturls():
	with open('songs.txt','r') as f:
		with open('songurls.txt','x') as f2:
			sys.stdout = f2
			for x in f:
				p = x.find('(')
				print(geturl(track=x[:p-1],year=x[p+1:p+5],artist=x[p+8:].title()))

if __name__ == "__main__":
	geturls()