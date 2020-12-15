from flask import Flask 
from app import config
from app import db

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)

    return app