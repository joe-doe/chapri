from werkzeug.security import generate_password_hash, check_password_hash


class User(object):

    def __init__(self, username, password="secret", is_authenticated=False):
        self._id = username
        self.password = generate_password_hash(password)
        self._is_authenticated = is_authenticated

    @property
    def is_authenticated(self):
        return self._is_authenticated
    
    @is_authenticated.setter
    def is_authenticated(self, flag):
        self._is_authenticated = flag

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self._id

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)

