import json
import os


class Config(object):
    def __init__(self, app):
        self.app = app
        self.load_defaults()
        self.override_env()
        
    def load_defaults(self):
        self.app.config['SECRET_KEY'] = 'secret!'
        # open configuration file, read the values and append to app.config
        with open('configuration/config.json') as config_file:
            self.config = json.load(config_file)
            self.app.config.update(self.config)

    def override_env(self):
        # get sensible credentials from environment variables
        try:
            self.config['MONGODB_URI'] = str(os.environ['MONGODB_URI'])
            self.app.config.update(self.config)
        except KeyError:
            pass
