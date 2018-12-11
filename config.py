import os

# config class
class Config(object):

    # sercet key needed for flask-wtf (CSRF)
    SECRET_KEY= os.environ.get('SECRET_KEY')
