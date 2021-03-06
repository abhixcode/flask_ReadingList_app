from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#from flaskblog.config import Config
from flask_ReadingList_app.config import Config



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	from flask_ReadingList_app.users.routes import users
	from flask_ReadingList_app.readinglist.routes import readinglist
	from flask_ReadingList_app.main.routes import main
	from flask_ReadingList_app.errors.handlers import errors
	app.register_blueprint(users)
	app.register_blueprint(readinglist)
	app.register_blueprint(main)
	app.register_blueprint(errors)

	return app
