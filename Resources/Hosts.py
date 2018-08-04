from os.path import isfile
import sys


class Hosts:

    def __init__(self, path):
        self.path = path
        self.check_path()
        self.sites = self.parse()

    def add(self, name):
        with open(self.path, "a") as hosts:
            hosts.write("\n127.0.0.1 " + name)

    def remove(self, name):
        with open(self.path, "r") as hosts:
            temp = hosts.readlines()
        new = [line for line in temp if name not in line]
        with(open(self.path, "w")) as new_hosts:
            new_hosts.writelines(new)


    def parse(self):
        with open(self.path, "r") as hosts:
            return [line.rstrip().split(" ") for line in hosts if not line.startswith("#") and line.strip()]

    def check_path(self):
        if not isfile(self.path):
            print(f"Could not find hosts file at {self.path}. Check config.")
            sys.exit(2)