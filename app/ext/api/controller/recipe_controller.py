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
from flask import session


def create_recipe(user_id, recipe):
    if not recipe.recipe_imgs:
        raise RecipeWithoutImage

    if len(recipe.recipe_imgs) > 6:
        raise MaximumImageCapacityError

    if not recipe.ingredients:
        raise RecipeWithoutIngredient

    if not recipe.preparation_mode:
        raise RecipeWithoutPreparationMode

    recipe_img_list = []

    for file in recipe.recipe_imgs:
        new_file = file_controller.create_file(file)
        recipe_file = recipe_services.create_recipe_files(new_file.get("id"))
        recipe_img_list.append(recipe_file)

    chef_id = recipe.chef_id

    if not chef_services.find_by_id(chef_id):
        raise ChefNotFound

    name = recipe.name
    ingredients = recipe.ingredients
    preparation_mode = recipe.preparation_mode
    additional_information = recipe.additional_information

    recipe = recipe_services.create_recipe(
        name,
        ingredients,
        preparation_mode,
        additional_information,
        chef_id,
        recipe_img_list,
        user_id,
    )

    session["audit_log"] = {
        "object_type": "RECIPE",
        "object_id": recipe.get("id"),
        "object_name": recipe.get("name"),
        "action": "CREATE",
    }

    return recipe


def update_recipe(recipe_id, user_id, recipe_data):
    recipe = recipe_services.find_by_id(recipe_id)
    files = recipe_data.recipe_imgs

    if not recipe:
        raise RecipeNotFound

    if recipe.user_id != user_id and not users_services.is_admin(user_id):
        raise OperationNotAllowed

    delete_imgs = recipe_data.delete_imgs

    if recipe_services.is_img_capacity_max(recipe_id, files, delete_imgs):
        raise MaximumImageCapacityError

    chef_id = recipe_data.chef_id

    if chef_id and not chef_services.find_by_id(chef_id):
        raise ChefNotFound

    ingredients = recipe_data.ingredients

    if len(ingredients) == 0:
        raise RecipeWithoutIngredient

    preparation_mode = recipe_data.preparation_mode

    if len(preparation_mode) == 0:
        raise RecipeWithoutPreparationMode

    name = recipe_data.name

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

    session["audit_log"] = {
        "object_type": "RECIPE",
        "object_id": recipe.get("id"),
        "object_name": recipe.get("name"),
        "action": "UPDATE",
    }

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

    session["audit_log"] = {
        "object_type": "RECIPE",
        "object_id": recipe.id,
        "object_name": recipe.id,
        "action": "DELETE",
    }

    recipe_services.delete_recipe(recipe_id)


def get_recipe(recipe_id):
    recipe = recipe_services.find_by_id(recipe_id)

    if not recipe:
        raise RecipeNotFound

    return recipe.as_dict()


def list_recipe():
    recipes = recipe_services.list_recipe()

    return {"recipes": recipes}
