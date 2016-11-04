from flask_socketio import SocketIO
from src.ws_routes import ChatNamespace


class WebSocket(object):

    def __init__(self, app):
        # Set async_mode to "threading", "eventlet" or "gevent" via config.json
        # to test the different async modes, or leave it set to None for the
        # application to choose the best option based on installed packages.
        
        self.socketio = SocketIO(app, async_mode=app.config['ASYNC_MODE'])
        self.socketio.on_namespace(ChatNamespace('/chat'))
