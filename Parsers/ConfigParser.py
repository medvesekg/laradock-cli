import sys
import os.path

class ConfigParser:

    _required = [
        'projects_path',
        'hosts_path',
        'laradock_path',
        'domain'
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

            self.config = self.normalize(config)

    def validate(self, config):
        for property in self._required:
            if property not in config:
                print(f"{property} missing from configuration.")
                sys.exit(2)

    def normalize(self, config):
        config['projects_path'] = self.remove_trailing_slash(self.remove_quotes(config['projects_path']))
        config['laradock_path'] = self.remove_trailing_slash(self.remove_quotes(config['laradock_path']))
        config['hosts_path'] = self.remove_trailing_slash(self.remove_quotes(config['hosts_path']))
        config['domain'] = self.prepend_dot(self.remove_quotes(config['domain']))
        return config

    def remove_trailing_slash(self, string):
        return string[:-1] if string.endswith(os.path.sep) else string

    def prepend_dot(self, string):
        return string if string.startswith(".") else "." + string

    def remove_quotes(self, string):
        if string.startswith("'") or string.startswith('"'):
            string = string[1:]
        if string.endswith("'") or string.endswith('"'):
            string = string[:-1]
        return string

    def get_laradock_path(self):
        return self.config['laradock_path']

    def get_hosts_path(self):
        return self.config['hosts_path']

    def get_domain(self):
        return self.config['domain']

    def get_projects_path(self):
        return self.config['projects_path']