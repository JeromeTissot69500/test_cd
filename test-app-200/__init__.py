import os

from flask import Flask
from .db.db import db, migrate
from .config.DevelopmentConfig import DevelopmentConfig
from .controller.login import login
from .controller.registration import registration
from .controller.index import index
from .controller.logout import logout
from .controller.user_account import user_account


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DevelopmentConfig)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('ProductionConfig.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_object(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(login)
    app.register_blueprint(registration)
    app.register_blueprint(index)
    app.register_blueprint(logout)
    app.register_blueprint(user_account)

    db.init_app(app)
    migrate.init_app(app, db)


    with app.app_context():
        db.create_all()

    return app
