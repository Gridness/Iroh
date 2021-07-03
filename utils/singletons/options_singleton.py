class Options():
    def __init__(self):
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 
        'options': '-vn'}
        self.YTDL_OPTIONS = {'format': 'bestaudio', 'skip_download': True}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Options, cls).__new__(cls)
        return cls.instance