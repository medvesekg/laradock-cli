import subprocess
from Commands.Command import Command

class Down(Command):

    def execute(self):
        subprocess.run("docker-compose down", shell=True, cwd=self.config.get_laradock_path())