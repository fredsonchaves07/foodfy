# from app.ext.api.controller import file_controller
from app.ext.api.exceptions import MaximumImageCapacityError, RecipeWithoutImage
from app.ext.api.services import recipe_services


def create_recipe(recipe, files):
    if not files:
        raise RecipeWithoutImage

    if len(files) > 6:
        raise MaximumImageCapacityError

    # TODO -> Verificar se o chef_id existe
    chef_id = recipe.get("chef_id")

    name = recipe.get("name")
    ingredients = recipe.getlist("ingredients")
    preparation_mode = recipe.getlist("preparation_mode")
    additional_information = recipe.get("additional_information")

    recipe = recipe_services.create_recipe(
        name, ingredients, preparation_mode, additional_information, chef_id
    )

    # for file in files:
    #     new_file = file_controller.create_file(file)

    return recipe
