from datetime import datetime
from app.db import db
from app.db.models import File, Recipe, RecipeFile


def create_recipe(name, chef_id, ingredients, preparations, adicional_information):
    recipe = Recipe(name=name, 
                    chef_id=chef_id, 
                    ingredients=ingredients,
                    preparations=preparations,
                    adicional_information=adicional_information)
    db.session.add(recipe)
    db.session.commit()
    
    return recipe.id


def create_recipe_file(recipe_id, file_id):
    recipe_file = RecipeFile(recipe_id=recipe_id, file_id=file_id)
    db.session.add(recipe_file)
    db.session.commit()
