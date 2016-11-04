from flask import Flask
from src.build import Builder


# Flask app
app = Flask(
    __name__,
    template_folder='src/templates'
)


application = Builder(app)

if __name__ == '__main__':
    application.get_socketio().run(app, debug=True)
