from flask import render_template


class Routes(object):
    
    def __init__(self, app):
        self.app = app
        self.index = app.route('/')(self.index)
        
    def index(self):
        return render_template(
            'index.html',
            async_mode=self.app.config['ASYNC_MODE']
        )
