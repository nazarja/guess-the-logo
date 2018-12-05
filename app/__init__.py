from flask import Flask

# initialise modules
app = Flask(__name__)

from app import routes