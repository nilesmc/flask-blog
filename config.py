# Define the application directory
import os
from os.path import join, dirname
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = join(basedir, '.env')
load_dotenv(dotenv_path)

class Config(object):
    # PSQL/SQL Alchemy Database Config
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    # WTForm Token
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email Config settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']

    # Defaults value for pagination
    POSTS_PER_PAGE = 3

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DATABASE_URL= os.environ.get('TEST_DATABASE_URL')
