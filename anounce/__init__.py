from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anounce.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'

db = SQLAlchemy(app)


from anounce import routes

