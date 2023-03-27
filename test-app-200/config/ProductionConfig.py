import os, secrets
from .Config import Config

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_TEST')
    TESTING = False
    DEBUG = False
    SECRET_KEY = secrets.token_hex(16)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_PATH = '/'