class VC():
    def __init__(self):
        self.vc = ""

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(VC, cls).__new__(cls)
        return cls.instance