from app.ext.api.controller import file_controller
from app.ext.api.exceptions import (
    ChefNotFound,
    MaximumImageCapacityError,
    OperationNotAllowed,
    RecipeNotFound,
    RecipeWithoutImage,
    RecipeWithoutIngredient,
    RecipeWithoutPreparationMode,
)
from app.ext.api.services import chef_services, recipe_services, users_services


def create_recipe(user_id, recipe, files):
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
        user_id,
    )

    return recipe


def update_recipe(recipe_id, user_id, recipe_data, files):
    recipe = recipe_services.find_by_id(recipe_id)

    if not recipe:
        raise RecipeNotFound

    if recipe.user_id != user_id and not users_services.is_admin(user_id):
        raise OperationNotAllowed

    delete_imgs = recipe_data.getlist("delete_imgs")

    if recipe_services.is_img_capacity_max(recipe_id, files, delete_imgs):
        raise MaximumImageCapacityError

    chef_id = recipe_data.get("chef_id")

    if chef_id and not chef_services.find_by_id(chef_id):
        raise ChefNotFound

    ingredients = recipe_data.getlist("ingredients")

    if len(ingredients) == 0:
        raise RecipeWithoutIngredient

    preparation_mode = recipe_data.getlist("preparation_mode")

    if len(preparation_mode) == 0:
        raise RecipeWithoutPreparationMode

    name = recipe_data.get("name")

    for file_id in delete_imgs:
        recipe_services.delete_recipe_files(recipe_id, file_id)
        file_controller.delete_file(file_id)

    recipe_img_list = []

    for file in files:
        new_file = file_controller.create_file(file)
        recipe_file = recipe_services.create_recipe_files(new_file.get("id"), recipe_id)
        recipe_img_list.append(recipe_file)

    recipe = recipe_services.update_recipe(
        recipe_id, name, chef_id, ingredients, preparation_mode, recipe_img_list
    )

    return recipe


def delete_recipe(recipe_id, user_id):
    recipe = recipe_services.find_by_id(recipe_id)

    if not recipe:
        raise RecipeNotFound

    if recipe.user_id != user_id and not users_services.is_admin(user_id):
        raise OperationNotAllowed

    for file in recipe.recipe_files:
        file_id = file.file_id

        recipe_services.delete_recipe_files(recipe_id, file_id)
        file_controller.delete_file(file_id)

    recipe_services.delete_recipe(recipe_id)


def get_recipe(recipe_id):
    recipe = recipe_services.find_by_id(recipe_id)

    if not recipe:
        raise RecipeNotFound

    return recipe.as_dict()


def list_recipe():
    recipes = recipe_services.list_recipe()

    return {"recipes": recipes}
