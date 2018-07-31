import subprocess
import json
from os.path import isfile
from Commands.Command import Command


class Up:

    def __init__(self, args, config):
        Command.__init__(self, args, config)
        self.presets = self.load_presets()

    def execute(self):

        containers = None
        if "default" in self.presets:
            containers = self.presets['default']
        if self.args.preset and self.args.preset in self.presets:
            containers = self.presets[self.args.preset]

        subprocess.run(f"docker-compose up -d {containers}", shell=True, cwd=self.config.get_laradock_path())

    def load_presets(self):
        if(isfile('presets.json')):
            with open("presets.json", "r") as file:
                presets = json.load(file)
                if "up" in presets:
                    return presets["up"]
        return None
