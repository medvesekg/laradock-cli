from Parsers.ConfigParser import ConfigParser
from Parsers.ArgParser import ArgParser
from Commands.CommandFactory import CommandFactory


config = ConfigParser("config.txt")
args = ArgParser().parse_args()

command = CommandFactory.create(args, config)
command.execute()



"""
import os
import sys
import shutil
from Site import Site
from Hosts import Hosts
from Folder import Folder

projects_path = "C:\\Koda\\laravel"
nginx_path = "C:\\Koda\\laravel\\laradock\\nginx\\sites"
hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
name = "newsite"

if(len(sys.argv) == 1):
    os.chdir("c:\\Koda\\laravel\\laradock")
    os.system("docker-compose up -d nginx workspace mysql redis phpmyadmin")
    exit()
if(len(sys.argv) == 2):
    os.chdir("c:\\Koda\\laravel\\laradock")
    os.system("docker-compose down")
    exit()

if(len(sys.argv) == 3):
    name = sys.argv[2]
    print("Project " + name + ":")

def get_sites(nginx_path):
    files = [file for file in os.listdir(nginx_path) if file.endswith(".conf")]
    return [Site(nginx_path + "/" + file) for file in files]

def create_site(name, preset):
    preset = nginx_path + "/" + preset + ".conf.example"
    path = nginx_path + "/" + name + ".conf"
    shutil.copyfile(preset, path)
    return path

site = Site(create_site(name, "laravel"))
site.set('server_name', name + ".test")
site.set('root', "/var/www/" + name + "/public")
site.save()
print('Created nginx conf at ' + nginx_path)

hosts = Hosts(hosts_path)
hosts.add(name + ".test")
print('Created hosts entry')
"""