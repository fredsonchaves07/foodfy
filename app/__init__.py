from dynaconf import FlaskDynaconf
from flask import Flask

dynaconf = FlaskDynaconf()


def create_app():
    app = Flask(__name__)
    dynaconf.init_app(app)

    return app
