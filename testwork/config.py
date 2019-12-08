import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = True
    SERVER_NAME = '127.0.0.1:8001'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'testwork.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CPU_USAGE_PER_PAGE = 100
    SECRET_KEY = 'testwork_secret'