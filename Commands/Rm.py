from Commands.Command import Command
from Resources.Hosts import Hosts
from Resources.Template import Template
import os
from pathlib import Path

class Rm(Command):

    def __init__(self, args, config):
        super().__init__(args, config)
        self.hosts = Hosts(self.config.get_hosts_path())
        self.presets = self.load_presets("new")

    def execute(self):

        self.hosts.remove(self.args.name + self.config.get_domain())
        print("Removed " + self.args.name + self.config.get_domain() + " from hosts file")

        preset = self.presets['default']

        for template in self.presets[preset]["templates"]:
            file = Template(self.args, self.config)
            destination = file.delete_dest(template)
            print("Removed " + destination._str)

        project_folder = Path(self.config.get_projects_path(), self.args.name)
        if(os.path.isdir(project_folder)):
            os.rmdir(project_folder)