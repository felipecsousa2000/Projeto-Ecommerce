from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
app.config["SECRET_KEY"] = '05e914aab8da1ba9dd24335b'
db.init_app(app)
bcrypt = Bcrypt(app)

from mercado import routes