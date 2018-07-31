from Commands.Command import Command
from Resources.Hosts import Hosts


class New(Command):

    def __init__(self, args, config):
        super().__init__(args, config)
        self.hosts = Hosts(self.config.get_hosts_path())

    def execute(self):
        self.hosts.add(self.args.name)
        print(self.hosts.sites)
        pass

        #update hosts file
        #update nginx conf
        #create dir
        #possibly install according to preset
        #restart laradock