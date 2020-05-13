import logging
import configparser
from pathlib import Path

from os.path import join, isdir,isfile, expanduser

class AppConfig():
    def __init__(self, appName, defaultDictValues=None):
        """ defaultDictValues will be loaded to the ini
            file if there isn't one already """
        # set up all of the things
        self.appname = appName
        self.appPath = str( Path(__file__).parent.absolute() )
        self.config = configparser.ConfigParser()
        config_name = "config.ini"
        config_file = Path(join( self.appPath, config_name ) )
        if config_file.is_file():
            #read from it
            self.config.read(str( config_file ))
        else:
            #make default one
            if defaultDictValues:
                logging.debug(defaultDictValues)
                for key, value in defaultDictValues.items():
                    for i, j in value.items():
                        self.config[key] = {i: j}

                with open(join(self.appPath, "config.ini"), 'w') as configfile:
                    self.config.write(configfile)


    def get(self, section,  key):
        # ability to get values from internal dictionary
        return self.config[section][key]
