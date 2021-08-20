import json

from app.ext.api.models.recipe import Recipe

# from app.ext.api.models.recipe_files import RecipeFiles
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
