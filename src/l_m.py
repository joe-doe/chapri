from flask import url_for
from flask_login import LoginManager
from database.model import User


class LoginManage(object):
    def __init__(self, app, db):
        self.app = app
        self.db = db
        
        self.l_m = LoginManager()
        self.l_m.login_view = 'signin'
        self.l_m.init_app(self.app)
        self.load_user = self.l_m.user_loader(self.load_user)
        
    def load_user(self, username):
        user = self.db[self.app.config['MONGODB_USERS_COLLECTION']].find_one(
            {"_id": username}
        )
        
        return User(user['_id'], is_authenticated=True) if user else None
