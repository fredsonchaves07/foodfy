from .main import admin
from .recipe import recipes
from .chef import chefs
from .auth import auth

def init_app(app):
    app.register_blueprint(admin)
    app.register_blueprint(recipes)
    app.register_blueprint(chefs)
    app.register_blueprint(auth)