class IsPlaying():
    def __init__(self):
        self.is_paying = False

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(IsPlaying, cls).__new__(cls)
        return cls.instance