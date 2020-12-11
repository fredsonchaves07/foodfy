from flask import Blueprint

recipes = Blueprint('recipes', __name__, url_prefix='/admin/recipes')

@recipes.route('/', methods=['GET'])
def index():
    return '<h1>Hello Recipe!</h1>'