from Commands.Enter import Enter
from Commands.Up import Up
from Commands.Down import Down
from Commands.New import New

class CommandFactory:

    @staticmethod
    def create(args, config):
        command_name = args.command.capitalize()
        return globals()[command_name](args, config)
