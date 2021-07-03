import youtube_dl

def search_yt(options, item):
    with youtube_dl.YoutubeDL(options) as ydl:
        try:
            info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
        except Exception:
            return False

    return {'source': info['formats'][0]['url'], 'title': info['title']}