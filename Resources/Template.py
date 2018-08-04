from pathlib import Path
import re
import os


class Template:


    def __init__(self, args, config):
        self.args = args
        self.config = config
        self.template_dir = Path(__file__).parents[1] / "Templates"
        pass

    def create_from(self, template):
        content = ""
        with open(self.template_dir / Path(template['source']), "r") as source:
            content = source.read()
        content = self.replace_variables(content)
        destination = self.config.get_laradock_path() / Path(self.replace_variables(template['dest']))
        with open(destination, "w") as file:
            file.write(content)
        return destination

    def replace_variables(self, text):
        processed = re.sub("{% * name *%}", self.args.name, text)
        processed = re.sub("{% * domain *%}", self.config.get_domain(), processed)
        return processed

    def delete_dest(self, template):
        destination = self.config.get_laradock_path() / Path(self.replace_variables(template['dest']))
        if(os.path.isfile(destination)):
            os.remove(destination)
        return destination
