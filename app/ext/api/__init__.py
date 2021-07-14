from flask import Blueprint


def init_app(app):
    user = Blueprint("user", __name__)
    app.register_blueprint(user, url_prefix="/api/v1/user")
