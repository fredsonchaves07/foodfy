from .main import admin
from .recipes import recipes

def init_app(app):
    app.register_blueprint(admin)
    app.register_blueprint(recipes)