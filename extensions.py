from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager




app = Flask(__name__)
app.config["SECRET_KEY"] = "d2613t7yt82u19ij4"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vachunchula.db"


db = SQLAlchemy(app)
login_manager = LoginManager(app)
