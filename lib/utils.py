import os
import yaml

def get_path(*args):
    return os.path.join(os.path.dirname(__file__), '..', *args)

def get_config():
    config_file = file(get_path('gezegen.yaml'), 'r')
    config = yaml.load(config_file)

    return config

