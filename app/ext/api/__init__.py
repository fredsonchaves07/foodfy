from .resources.user import user_api


def init_app(app):
    app.register_blueprint(user_api, url_prefix="/api/v1/user")
