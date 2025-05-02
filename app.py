from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
from pymongo import MongoClient
from googleapiclient.discovery import build
from Controllers.youtubeControllers import postYoutubeData

load_dotenv()

# .env
client_id = os.getenv("SPOTIFY_ID")
client_secret = os.getenv("SPOTIFY_SECRET")

# Autenticando ao MongoDB
client = MongoClient(os.getenv("MONGO_URI"))

# Autenticando ao Youtube
service = build("youtube", "v3", developerKey=os.getenv("YOUTUBE_KEY"))

# Autenticando ao Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Database e Collection
db = client["atv-spotify-yt"]

artist = "https://open.spotify.com/artist/3YQKmKGau1PzlVlkL1iodx?si=G12ImuQzQjyShV1150Tp1g"

items = sp.artist_albums(artist_id=artist, album_type="album")["items"]

collection = service.videos().list(
    part="snippet",
    chart="mostPopular",
    regionCode="BR",
    maxResults=5,
    videoCategoryId="10"
)

response = collection.execute()

postYoutubeData(response, db)
postYoutubeData(response["items"])

# postYoutubeData(response["items"])
# Testar respostas
print(type(response["items"]))