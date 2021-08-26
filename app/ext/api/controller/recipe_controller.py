from app.ext.api.controller import file_controller
from app.ext.api.exceptions import (
    ChefNotFound,
    MaximumImageCapacityError,
    RecipeWithoutImage,
    RecipeWithoutIngredient,
    RecipeWithoutPreparationMode,
)
from app.ext.api.services import chef_services, recipe_services


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

    chef_id = recipe.get("chef_id")

    if not chef_services.find_by_id(chef_id):
        raise ChefNotFound

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


def update_recipe(recipe_id, recipe_data, files):

    name = recipe_data.get("name")
    delete_imgs = recipe_data.getlist("delete_imgs")

    for file_id in delete_imgs:
        recipe_services.delete_recipe_files(recipe_id, file_id)
        file_controller.delete_file(file_id)

    recipe_img_list = []

    for file in files:
        new_file = file_controller.create_file(file)
        recipe_file = recipe_services.create_recipe_files(new_file.get("id"), recipe_id)
        recipe_img_list.append(recipe_file)

    recipe = recipe_services.update_recipe(recipe_id, name, recipe_img_list)

    return recipe
