from flask import render_template


def init_routes(app, socketio_async_mode):
    @app.route('/')
    def index():
        return render_template('index.html', async_mode=socketio_async_mode)
