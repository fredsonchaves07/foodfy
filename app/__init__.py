from flask import Flask
from dynaconf import FlaskDynaconf


dynaconf = FlaskDynaconf()


def create_app():
    app = Flask(__name__)
    dynaconf.init_app(app)

    return app
