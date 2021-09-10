from .controller import error_handler
from .exceptions import BadRequestError
from .resources.auth import auth_api
from .resources.chef import chef_api
from .resources.recipe import recipe_api
from .resources.user import user_api


def init_app(app):
    app.register_blueprint(user_api, url_prefix="/api/v1/user")
    app.register_blueprint(auth_api, url_prefix="/api/v1/auth")
    app.register_blueprint(chef_api, url_prefix="/api/v1/chef")
    app.register_blueprint(recipe_api, url_prefix="/api/v1/recipe")

    app.register_error_handler(404, error_handler.url_not_found)
    app.register_error_handler(405, error_handler.method_not_allowed)
    app.register_error_handler(500, error_handler.server_error)

    app.register_error_handler(BadRequestError, error_handler.response_error)
    app.register_error_handler(Exception, error_handler.server_error)
