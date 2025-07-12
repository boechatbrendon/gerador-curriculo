from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ASDFGHJJKLIU123456789'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///curriculos.db'

db = SQLAlchemy(app)


from app import routes