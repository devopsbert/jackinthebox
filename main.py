#!/usr/bin/python
from modules.fixture import SimpleFixture
import git
import yaml

#load config
with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

#check latest code
repo = git.Repo(search_parent_directories=True)
origin = repo.remotes['origin']
origin.pull()
sha = repo.head.object.hexsha
if sha != cfg['git_hash']:
    print('You should update your code!')

#def main():
light = SimpleFixture({'id': 1, 'name': 'Infra', 'state': 1})





