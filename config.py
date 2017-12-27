import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # WTForms token
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # PSQL/SQL Alchemy Database Config
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://localhost/dev_flask-blog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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
