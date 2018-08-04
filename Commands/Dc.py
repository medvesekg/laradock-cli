from Commands.Command import Command
import subprocess


class Dc(Command):

    def execute(self):
        subprocess.run("docker-compose " + " ".join(self.args.commands), shell=True, cwd=self.config.get_laradock_path())