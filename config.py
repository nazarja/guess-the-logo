import os


# config class
class Config(object):

    # sercet key needed for CSRF protection
    SECRET_KEY= os.environ.get('SECRET_KEY')
