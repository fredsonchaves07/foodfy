from dynaconf import FlaskDynaconf
from flask import Flask

from app.ext import api, db

dynaconf = FlaskDynaconf()


def create_app():
    app = Flask(__name__)
    dynaconf.init_app(app)
    api.init_app(app)
    db.init_app(app)

    return app
