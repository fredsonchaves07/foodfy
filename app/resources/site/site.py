from flask import Blueprint, request, render_template, redirect, url_for
from app.controllers.admin import recipe as recipe_controller
from app.controllers.admin import chef as chef_controller


site = Blueprint('site', __name__, url_prefix='/')


@site.app_errorhandler(404)
def page_not_found(e):
    return render_template('site/404.html'), 404


@site.app_errorhandler(500)
def internal_error_serve(e):
    return render_template('site/500.html'), 500


@site.route('/', methods=['GET'])
def index():
    recipes = recipe_controller.list_recipes()
    
    return render_template('site/index.html', recipes=recipes)


@site.route('/about', methods=['GET'])
def about():
    return render_template('site/about.html')


@site.route('/filter', methods=['GET'])
def filtro():
    data_filter = request.args['filter']

    recipes = recipe_controller.filter_recipe(data_filter)
    
    return render_template('site/filter.html', recipes=recipes, filter=data_filter)


@site.route('/recipes', methods=['GET'])
def list_recipes():
    recipes = recipe_controller.list_recipes()
    
    return render_template('site/recipe.html', recipes=recipes)


@site.route('/recipes/<recipe_id>', methods=['GET'])
def show_recipe(recipe_id):
    recipe = recipe_controller.show_recipe(recipe_id)
    
    return render_template('site/view-recipe.html', recipe=recipe)


@site.route('/chefs', methods=['GET'])
def list_chefs():
    chefs = chef_controller.list_chefs()
    
    return render_template('site/chef.html', chefs=chefs)


@site.route('/chefs/<chef_id>', methods=['GET'])
def show_chef(chef_id):
    chef = chef_controller.show_chef(chef_id)
    
    return render_template('site/view-chef.html', chef=chef)


