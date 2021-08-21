import json

from app.ext.api.models.recipe import Recipe
from app.ext.api.models.recipe_files import RecipeFiles
from app.ext.database import db


def create_recipe(name, ingredients, preparation_mode, additional_information, chef_id):
    recipe = Recipe()

    recipe.name = name
    recipe.ingredients = json.dumps(ingredients)
    recipe.preparation_mode = json.dumps(preparation_mode)
    recipe.additional_information = additional_information
    recipe.chef_id = chef_id

    db.session.add(recipe)
    db.session.commit()

    return recipe.as_dict()


def create_recipe_files(file_id, recipe_id):
    recipe_file = RecipeFiles()

    recipe_file.file_id = file_id
    recipe_file.recipe_id = recipe_id

    db.session.add(recipe_file)
    db.session.commit()

    return recipe_file


def find_by_id(recipe_id):
    recipe = Recipe.query.filter_by(id=recipe_id).first()

    return recipe


def update_recipe_img(recipe_id, img_list):
    recipe = find_by_id(recipe_id)
    recipe.recipe_files = img_list

    db.session.add(recipe)
    db.session.commit()
