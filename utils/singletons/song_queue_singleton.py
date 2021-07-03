class SongQueue():
    def __init__(self):
        self.song_queue = []

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SongQueue, cls).__new__(cls)
        return cls.instance