from app.dao import chef as chef_dao
from app.dao import recipe as recipe_dao
from app.controllers.admin import file as file_controller

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
    

def list_chef_recipe():
    chefs = chef_dao.all_chef() 

    return [(chef[0], chef[2]) for chef in chefs]
