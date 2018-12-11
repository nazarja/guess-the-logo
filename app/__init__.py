from flask import Flask
from config import Config

'''
    initalise application and imported modules
    routes and errors are imported at the bottom
    as the app and config must be initalised first
'''

#=====================#


# initialise modules
app = Flask(__name__)
app.config.from_object(Config)

# import local modules
from app import routes, errors