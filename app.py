from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from pprint import pprint

load_dotenv()

client_id = os.getenv("SPOTIFY_ID")
client_secret = os.getenv("SPOTIFY_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

artist = "https://open.spotify.com/artist/3YQKmKGau1PzlVlkL1iodx?si=G12ImuQzQjyShV1150Tp1g"

result = sp.artist_albums(artist_id=artist, album_type="album")

pprint(result["items"][0]["name"])

# album = result.
