from app.ext.api.controller import file_controller
from app.ext.api.exceptions import (
    MaximumImageCapacityError,
    RecipeWithoutImage,
    RecipeWithoutIngredient,
    RecipeWithoutPreparationMode,
)
from app.ext.api.services import recipe_services


def create_recipe(recipe, files):
    if not files:
        raise RecipeWithoutImage

    if len(files) > 6:
        raise MaximumImageCapacityError

    if not recipe.getlist("ingredients"):
        raise RecipeWithoutIngredient

    if not recipe.getlist("preparation_mode"):
        raise RecipeWithoutPreparationMode

    recipe_img_list = []

    for file in files:
        new_file = file_controller.create_file(file)
        recipe_file = recipe_services.create_recipe_files(
            new_file.get("id"), recipe.get("id")
        )
        recipe_img_list.append(recipe_file)

    # TODO -> Verificar se o chef_id existe
    chef_id = recipe.get("chef_id")
    name = recipe.get("name")
    ingredients = recipe.getlist("ingredients")
    preparation_mode = recipe.getlist("preparation_mode")
    additional_information = recipe.get("additional_information")

    recipe = recipe_services.create_recipe(
        name,
        ingredients,
        preparation_mode,
        additional_information,
        chef_id,
        recipe_img_list,
    )

    return recipe
