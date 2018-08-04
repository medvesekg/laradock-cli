import subprocess
import json
from os.path import isfile
from Commands.Command import Command


class Up(Command):

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

