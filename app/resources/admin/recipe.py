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

        return redirect(url_for('recipes.show_recipe', recipe_id=recipe_id))

    return render_template('admin/recipe/create.html', form=form)


@recipes.route('/<recipe_id>', methods=['GET'])
def show_recipe(recipe_id):
    recipe = recipe_controller.show_recipe(recipe_id)
    
    return render_template('admin/recipe/view.html', recipe=recipe)


@recipes.route('/<recipe_id>/edit', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    pass
    # chef = chef_controler.show_chef(chef_id)
    # form = RegistrationChef(obj=chef)
    # file = request.files
    
    # if request.method == 'POST':
    #     if request.form['_method'] == 'PUT':
    #         chef_controler.edit_chef(chef_id, file, form)

    #         return redirect(url_for('chefs.show_chef', chef_id=chef_id))
        
    #     if request.form['_method'] == 'DELETE':
    #         chef_controler.delete_chef(chef_id)

    #         return redirect(url_for('chefs.list_chefs'))
        

    # return render_template('admin/chef/edit.html', chef=chef, form=form)