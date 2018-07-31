from argparse import ArgumentParser

class ArgParser:

    def __init__(self):

        self.parser = ArgumentParser(prog="PROG")
        subparsers = self.parser.add_subparsers(help="sub-command help", dest="command")
        subparsers.required = True

        subparser_up = subparsers.add_parser('up')
        subparser_up.add_argument("--preset")

        subparser_down = subparsers.add_parser('down')

        subparser_enter = subparsers.add_parser('enter')

        subparser_new = subparsers.add_parser('new')
        subparser_new.add_argument("name")
        subparser_new.add_argument("--preset")

        subparser_rm = subparsers.add_parser('rm')
        subparser_rm.add_argument("name")

    def parse_args(self):
        return self.parser.parse_args()