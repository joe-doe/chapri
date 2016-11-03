from flask import Flask
from flask_socketio import SocketIO
from src.websockets_routes import ChatNamespace
from src.routes import init_routes


# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

# Flask app
app = Flask(
    __name__,
    template_folder='src/templates'
)
app.config['SECRET_KEY'] = 'secret!'

# Flask-socketio
socketio = SocketIO(app, async_mode=async_mode)
socketio.on_namespace(ChatNamespace('/chat'))

# Common routes
init_routes(app, socketio.async_mode)

if __name__ == '__main__':
    socketio.run(app, debug=True)