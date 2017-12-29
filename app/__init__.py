import os
from flask import Flask
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
csrf = CSRFProtect()
login = LoginManager()
login.session_protection = "strong"
login.login_view = "main.login"

def create_app(config_name):
	app = Flask(__name__, static_url_path="/static")
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	
	bootstrap.init_app(app)
	db.init_app(app)
	csrf.init_app(app)
	login.init_app(app)	

	from .main import main as main_blueprint
	from .auth import auth 
	app.register_blueprint(main_blueprint)
	app.register_blueprint(auth, url_prefix="/auth")
	
	return app





