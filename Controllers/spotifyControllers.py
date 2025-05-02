# Post dados Spotify
def postSpotifyData(response, db):
    collection = db["spotify"]
    for item in response:
        
        collection.insert_one(item)
