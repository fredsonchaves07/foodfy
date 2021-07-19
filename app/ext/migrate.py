from app.ext import db

# from app.ext.api import models  # noqa
from flask_migrate import Migrate

migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)
