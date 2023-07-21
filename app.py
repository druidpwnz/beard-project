# TODO generate content for site with chatgpt
# TODO add flask-login for login into admin page
# TODO add feedback page and feedback form
# TODO move models, forms and views to different modules

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///beard.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from views import *
