from app.dao import chef as chef_dao
from app.dao import recipe as recipe_dao
from app.controllers.admin import file as file_controller

def list_chefs():
    chefs = chef_dao.all_chef()

    return chefs

def create_chef(form, file):
    chef_name = form.name.data
    chef_avatar = file['avatar']
    file_id = file_controller.create_file(chef_avatar)
    
    return chef_dao.create_chef(name=chef_name, file_id=file_id)

def show_chef(chef_id):
    chef = chef_dao.find_chef(chef_id)
    file = file_controller.find_file(chef.file_id)
    list_recipes_chef = recipe_dao.list_recipes_chef(chef_id)
    list_recipes = []
    
    for recipe in list_recipes_chef:
        image = recipe_dao.find_recipe_file(recipe.id)[0]
        
        recipes = {
            'id': recipe.id,
            'name': recipe.name,
            'image': image.file.name
        }
        
        list_recipes.append(recipes)
    
    chef.avatar = file.name
    chef.recipes = list_recipes
    
    return chef

def edit_chef(chef_id, file, form):
    chef_name = form.name.data
    new_file = file['avatar']
    
    if new_file:
        chef = chef_dao.find_chef(chef_id)
        old_file = file_controller.find_file(chef.file_id)
        file_controller.update_file(new_file, old_file)
        
    return chef_dao.update_chef(chef_id, chef_name)


def delete_chef(chef_id):
    chef = show_chef(chef_id)
    file = file_controller.find_file(chef.file_id)
    chef_dao.delete_chef(chef)
    file_controller.remove_file(file)
    # Verificia se existe receita. Exclusão não pode realizar se tiver receita
    return

    
