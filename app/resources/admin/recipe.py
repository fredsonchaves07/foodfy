from flask import Blueprint, request, render_template, redirect, url_for
from app.controllers.admin.form import RegistrationRecipe
from app.controllers.admin import recipe

recipes = Blueprint('recipes', __name__, url_prefix='/admin/recipes')


@recipes.route('/', methods=['GET'])
def list_recipes():
    return render_template('admin/recipes/index')


@recipes.route('/create', methods=['GET', 'POST'])
def create_recipe():
    form = RegistrationRecipe(request.form)
    file = request.files
    
    if request.method == 'POST':
        # chef_id = chef_controler.create_chef(form, file)

        # return redirect(url_for('chefs.show_chef', chef_id=chef_id))
        print(request.files)
        print(form.data)
    return render_template('admin/recipe/create.html', form=form)