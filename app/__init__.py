from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import hashlib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = hashlib.sha3_512(os.urandom(24)).hexdigest()  # creates a hash of a pseudo random value
# using the sha3 implementation
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lab5:lab5@localhost/lab5"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
