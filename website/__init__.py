from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='dasfSSdsS DDADSFDwsdx'
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    #import the blueprint objects
    from .views import views
    from .auth import auth
    '''Instead of putting all your routes and logic into a single app.py
     separate them into files which can be accessed with the url prefix 
     ahead of (and also auth/views etc instead of app)it using blueprints.'''
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User, Note
    create_database(app)

    #setting up flask login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    '''decorator to load the user object from databasee when id given,
    automatially registers the unction with flask login'''
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not os.path.exists('website/' + DB_NAME):
        with app.app_context():
            #creates all tables in model
            db.create_all()
            print('Created Database!')