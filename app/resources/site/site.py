from flask import Blueprint, request, render_template, redirect, url_for
from app.controllers.admin import recipe as recipe_controller
from app.controllers.admin import chef as chef_controller


site = Blueprint('site', __name__, url_prefix='/')


@site.route('/', methods=['GET'])
def index():
    recipes = recipe_controller.list_recipes()
    
    return render_template('site/index.html', recipes=recipes)


@site.route('/about', methods=['GET'])
def about():
    return render_template('site/about.html')


@site.route('/recipes', methods=['GET'])
def recipes():
    recipes = recipe_controller.list_recipes()
    
    return render_template('site/recipe.html', recipes=recipes)


@site.route('/chefs', methods=['GET'])
def chefs():
    chefs = chef_controller.list_chefs()
    
    return render_template('site/chef.html', chefs=chefs)