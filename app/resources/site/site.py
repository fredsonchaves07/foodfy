from flask import Blueprint, request, render_template, redirect, url_for
from app.controllers.admin import recipe as recipe_controller


site = Blueprint('site', __name__, url_prefix='/')


@site.route('/about', methods=['GET'])
def index():
    return render_template('site/about.html')


@site.route('/recipes', methods=['GET'])
def recipes():
    recipes = recipe_controller.list_recipes()
    
    return render_template('site/recipe.html', recipes=recipes)