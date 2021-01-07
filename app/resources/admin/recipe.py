from flask import Blueprint, request, render_template, redirect, url_for
from app.controllers.admin.form import RegistrationRecipe
from app.controllers.admin import recipe as recipe_controller

recipes = Blueprint('recipes', __name__, url_prefix='/admin/recipes')


@recipes.route('/', methods=['GET'])
def list_recipes():
    return render_template('admin/recipes/index')


@recipes.route('/create', methods=['GET', 'POST'])
def create_recipe():
    form = RegistrationRecipe(request.form)
    form.chef.choices = form.chef.choices + recipe_controller.list_chef_recipe()
    file = request.files
    
    if request.method == 'POST':
        recipe_id = recipe_controller.create_recipe(form, file)

        return 'ok'
        return redirect(url_for('recipes.show_recipe', recipe_id=recipe_id))

    return render_template('admin/recipe/create.html', form=form)