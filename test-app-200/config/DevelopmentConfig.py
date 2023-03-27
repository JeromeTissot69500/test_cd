import os
from .Config import Config


class DevelopmentConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Development_2023@localhost:5432/testcd"
    SECRET_KEY = 'dev'
    DEBUG = True
    APPLICATION_ROOT = '/connexion'
    TEMPLATES_AUTO_RELOAD = True
    SESSION_COOKIE_PATH = '/'

