from flask import Flask
from config import Config
from flask_moment import Moment


# initialise modules
app = Flask(__name__)
app.config.from_object(Config)
moment = Moment(app)


# import app mvc modules
from app import routes, errors