from os.path import isfile
import sys


class Hosts:

    def __init__(self, path):
        self.path = path
        self.check_path()
        self.sites = self.parse()

    def add(self, name):
        with open(self.path, "a") as hosts:
            hosts.write("127.0.0.1 " + name + "\n")

    def parse(self):
        with open(self.path, "r") as hosts:
            return [line.rstrip().split(" ") for line in hosts if not line.startswith("#") and line.strip()]

    def check_path(self):
        if not isfile(self.path):
            print("Could not find hosts file. Check config.")
            sys.exit(2)