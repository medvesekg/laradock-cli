import os

class Folder:

    def __init__(self, path):
        self.path = path
        self.folders = os.listdir(path)