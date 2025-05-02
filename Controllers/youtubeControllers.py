# Post dados Youtube
def postYoutubeData(response, db):
    try:
        collection = db["youtube"]
        for item in response["items"]:
            post = {
                "titulo": item["snippet"]["title"],
                "descricao": item["snippet"]["description"],
                "canal": item["snippet"]["channelTitle"],
                "data": item["snippet"]["publishedAt"],
                "link": f"https://www.youtube.com/watch?v={item['id']}",
                "thumbnail": item["snippet"]["thumbnails"]["default"]["url"],
            }
            collection.insert_one(post)
    except Exception as e:
        print(f"Erro ao inserir dados no MongoDB: {e}")
