import json
from os.path import isfile

class Command:
    def __init__(self, args, config):
        self.args = args
        self.config = config

    def load_presets(self, name=None):
        name = name if name else self.__class__.__name__.lower()
        if(isfile('presets.json')):
            with open("presets.json", "r") as file:
                presets = json.load(file)
                if name in presets:
                    return presets[name]
        return None