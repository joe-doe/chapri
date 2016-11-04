from configuration.configuration import Config
from database.db import Mongodb
from ws import WebSocket
from routes import Routes
from ws_routes import ChatNamespace

class Builder(object):
    
    def __init__(self, app):
        self.app = app
        self.load_config()
        self.initialize_db()
        self.initialize_ws()
        self.init_routes()
    
    def load_config(self):
        self.config = Config(self.app)

    def initialize_db(self):
        # establish mongoDB connection
        config = self.app.config
        self.db = Mongodb(config['MONGODB_URI'], config['MONGODB_DB'])

    def initialize_ws(self):
        self.ws = WebSocket(self.app, self.db.get_db())
        
    def init_routes(self):
        self.routes = Routes(self.app)
        
    def get_db(self):
        return self.db.get_db()
    
    def get_socketio(self):
        return self.ws.socketio
