from flask import render_template, redirect, url_for, request, flash
from cgi import escape

from flask_login import logout_user
from pymongo.errors import DuplicateKeyError

from database.model import User
from flask_login import login_user, login_required


class Routes(object):
    
    def __init__(self, app, db):
        self.app = app
        self.db = db
        
        self.index = app.route('/')(self.index)
        self.signin = app.route('/signin')(self.signin)
        self.signout = app.route('/signout')(self.signout)
        self.welcome = app.route('/welcome')(self.welcome)
        self.validate_login = app.route('/validate_login')(self.validate_login)
        self.register = app.route('/register')(self.register)
        self.registration = app.route('/registration')(self.registration)
    
    @login_required
    def index(self):
        return render_template(
            'index.html',
            async_mode=self.app.config['ASYNC_MODE']
        )

    @login_required
    def welcome(self):
        return render_template('welcome.html')
    
    def signin(self):
        return render_template('signin.html')

    def signout(self):
        logout_user()
        return render_template('signin.html')

    def validate_login(self):
        data = request.args
        username = escape(data.get('username'))
        password = escape(data.get('password'))
        
        user_in_db = self.db[
            self.app.config['MONGODB_USERS_COLLECTION']].find_one(
            {"_id": username}
        )
        
        if user_in_db:
            if User.validate_login(user_in_db.get('password'), password):
                user = User(username, password)
                login_user(user)
                return redirect(url_for('welcome'))
            else:
                flash("invalid credentials", category="alert alert-danger")
                return redirect(url_for('signin'))
        else:
            flash("never registered", category="alert alert-danger")
            return redirect(url_for('signin'))

    @login_required
    def registration(self):
        return render_template('registration.html')
    
    @login_required
    def register(self):
        data = request.args
        username = escape(data.get('username'))
        password = escape(data.get('password'))

        user = User(username, password)
        try:
            self.db[self.app.config['MONGODB_USERS_COLLECTION']].insert(
                {
                    "_id": user._id,
                    "password": user.password
                }
            )
        except DuplicateKeyError:
            print "User already present in DB."
        
        return redirect(url_for('welcome'))
