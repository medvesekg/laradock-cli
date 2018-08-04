from Commands.Command import Command
from Resources.Hosts import Hosts
from Resources.Template import Template
from pathlib import Path
import subprocess
import os



class New(Command):

    def __init__(self, args, config):
        super().__init__(args, config)
        self.hosts = Hosts(self.config.get_hosts_path())
        self.presets = self.load_presets()

    def execute(self):


        self.hosts.add(self.args.name + self.config.get_domain())
        print("Added " + self.args.name + self.config.get_domain() + " to hosts file")

        preset = self.args.preset if self.args.preset else self.presets['default']

        for template in self.presets[preset]['templates']:
            file = Template(self.args, self.config)
            destination = file.create_from(template)
            print("Added " + destination._str)

        project_folder = Path(self.config.get_projects_path(), self.args.name)
        os.mkdir(project_folder)
        print("Created " + project_folder._str)

        subprocess.run(self.presets[preset]['install'], shell=True, cwd=project_folder)


        subprocess.run("docker-compose restart", shell=True, cwd=self.config.get_laradock_path())