import sys

class ConfigParser:

    _required = [
        'projects_path',
        'hosts_path',
        'laradock_path'
    ]

    def __init__(self, config_file):
        self.parse(config_file)


    def parse(self, config_file):
        with open(config_file, "r") as fp:
            config = {}
            for line in fp.readlines():
                try:
                    components = line.split("=")
                    config[components[0].strip()] = components[1].strip()
                except:
                    print("Could not parse configuration file")

            self.validate(config)
            self.config = config

    def validate(self, config):
        for property in self._required:
            if property not in config:
                print(f"{property} missing from configuration.")
                sys.exit(2)


    def get_laradock_path(self):
        return self.config['laradock_path']

    def get_hosts_path(self):
        return self.config['hosts_path']

