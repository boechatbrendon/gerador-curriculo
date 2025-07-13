from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ASDFGHJJKLIU123456789'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///curriculos.db'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app import routes