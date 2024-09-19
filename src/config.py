from pathlib import Path
from dataclasses import dataclass
from configparser import ConfigParser
from platform import system

HOME_DIRECTORY = Path.home()
CONFIG_PATH =  HOME_DIRECTORY / Path('.config/hxm')
CONFIG_FILE = CONFIG_PATH / Path('hxm.conf')
DEFAULT_DB_PATH = CONFIG_PATH / Path('.config')
        
class Config: 
    
    def load_existing_config():
        config = ConfigParser()
        with open(CONFIG_FILE, 'r') as config_file:
            config.read(config_file)
            return config

    def create_new_config():
        config = ConfigParser()
        CONFIG_PATH.mkdir(exist_ok=True, parents=True)
        with open(CONFIG_FILE, 'w') as config_file:
            config['GENERAL'] = {}
            general = config['GENERAL']
            general['platform'] = system()
            general['trusted_authority'] = 'hxm.patchwork-security.de'
            general['db_file_path'] = DEFAULT_DB_PATH.name
            config.write(config_file)
            return config
        

def load_config():
    if CONFIG_FILE.exists():
        config = Config.load_existing_config()
        return config
    else:
        config = Config.create_new_config()
        return config

load_config()


