from app.dao import chef as chef_dao
from app.dao import recipe as recipe_dao
from app.controllers.admin import file as file_controller


def list_recipes():
    recipes = recipe_dao.all_recipes()

    for recipe in recipes:
        recipe_files_img = recipe_dao.find_recipe_file(recipe.id)

        if recipe_files_img:
            recipe.recipe_img = recipe_files_img[0].file.name

    return recipes


def list_chef_recipe():
    chefs = chef_dao.all_chef() 

    return [(chef[0], chef[2]) for chef in chefs]


def create_recipe(form, file):
    recipe_name = form.name.data
    recipe_chef = form.chef.data
    recipe_ingredients = form.ingredients.data
    recipe_preparations = form.preparations.data
    recipe_adicional_information = form.adicional_information.data

    recipe_id = recipe_dao.create_recipe(name=recipe_name, 
                                         chef_id=recipe_chef,
                                         ingredients=recipe_ingredients,
                                         preparations=recipe_preparations,
                                         adicional_information=recipe_adicional_information)

    for recipe_img in file.getlist('recipe_img'):
        file_id = file_controller.create_file(recipe_img)
        recipe_dao.create_recipe_file(recipe_id=recipe_id, file_id=file_id)
    
    return recipe_id


def show_recipe(recipe_id):
    files = []
    recipe = recipe_dao.find_recipe(recipe_id)
    chef = chef_dao.find_chef(recipe.chef_id)
    recipe_files = recipe_dao.find_recipe_file(recipe_id)
    recipe.chef_name = chef.name

    for recipe_file in recipe_files:
        file = file_controller.find_file(recipe_file.file_id)
        files.append(file)

    recipe.recipe_img = files
    
    return recipe
    

def edit_recipe(recipe_id, files, removed_files, form):
    recipe_name = form.name.data
    recipe_chef = form.chef.data
    recipe_ingredients = form.ingredients.data
    recipe_preparations = form.preparations.data
    recipe_adicional_information = form.adicional_information.data
    remove_files_id = removed_files.split(',')  

    for recipe_img in files.getlist('recipe_img'):
        if recipe_img.filename:
            file_id = file_controller.create_file(recipe_img)
            recipe_dao.create_recipe_file(recipe_id=recipe_id, file_id=file_id)
    
    if removed_files:
        for file_id in remove_files_id:
            recipe_dao.remove_recipe_file(recipe_id=recipe_id, file_id=file_id)
      
               
    return recipe_dao.update_recipe(recipe_id=recipe_id, 
                                    name=recipe_name,
                                    chef_id=recipe_chef,
                                    ingredients=recipe_ingredients,
                                    preparations=recipe_preparations,
                                    adicional_information=recipe_adicional_information)
    
    
def delete_recipe(recipe_id):
    recipe = show_recipe(recipe_id)
    list_recipe_imgs = recipe.recipe_img
    
    for file in list_recipe_imgs:
        recipe_dao.remove_recipe_file(recipe_id=recipe_id, file_id=file.id)
        file_controller.remove_file(file)
    
    recipe_dao.delete_recipe(recipe)


def filter_recipe(data_filter):
    recipes = recipe_dao.filter_recipe(data_filter)

    for recipe in recipes:
        recipe_files_img = recipe_dao.find_recipe_file(recipe.id)

        if recipe_files_img:
            recipe.recipe_img = recipe_files_img[0].file.name

    return recipes
