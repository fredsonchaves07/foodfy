from .resources.auth import auth_api
from .resources.user import user_api


def init_app(app):
    app.register_blueprint(user_api, url_prefix="/api/v1/user")
    app.register_blueprint(auth_api, url_prefix="/api/v1/auth")
