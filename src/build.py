from configuration.configuration import Config
from database.db import Mongodb
from ws import WebSocket
from routes import Routes
from l_m import LoginManage


class Builder(object):
    
    def __init__(self, app):
        self.app = app
        
        self.load_config()

        self.initialize_db()
        self.initialize_login_manager()
        self.initialize_ws()
        self.init_routes()

    def load_config(self):
        self.config = Config(self.app)
    
    def initialize_login_manager(self):
        self.l_m = LoginManage(self.app, self.db)
        
    def initialize_db(self):
        # establish mongoDB connection
        config = self.app.config
        database = Mongodb(config['MONGODB_URI'], config['MONGODB_DB'])
        self.db = database.get_db()
        
    def initialize_ws(self):
        self.ws = WebSocket(self.app, self.db)
        
    def init_routes(self):
        self.routes = Routes(self.app, self.db)
        
    def get_db(self):
        return self.db
    
    def get_socketio(self):
        return self.ws.socketio
