from Commands.Command import Command
import subprocess


class Enter(Command):

    def execute(self):
        subprocess.run("docker-compose exec workspace bash", shell=True, cwd=self.config.get_laradock_path())
