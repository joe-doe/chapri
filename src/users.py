from database.model import User


class Users(object):
    def __init__(self, app, db):
        self.app = app
        self.db = db
    
    def register_user(self, username, password):
        user = User(username, password)
        self.db[self.app.config['MONGODB_USERS_COLLECTION']].insert(
            {
                "_id": user._id,
                "password": user.password
            }
        )
