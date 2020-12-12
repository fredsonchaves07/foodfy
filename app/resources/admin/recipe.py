from app.controllers.admin import recipe
from flask import Blueprint

recipes = Blueprint('recipes', __name__, url_prefix='/admin/recipes')

@recipes.route('/', methods=['GET'])
def list_recipes():
    return render_template('admin/recipes/index')