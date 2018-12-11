from flask import Flask
from config import Config

# initialise modules
app = Flask(__name__)
app.config.from_object(Config)

# import app mvc modules
from app import routes, errors