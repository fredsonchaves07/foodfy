from app.ext.api.controller import recipe_controller
from app.ext.api.decorators import audit_log, authentication
from app.ext.api.schemas.recipe_schemas import CreateRecipeSchema, UpdateRecipeSchema
from flask import Blueprint, request

recipe_api = Blueprint("recipe", __name__)


@recipe_api.route("", methods=["POST"])
@authentication
@audit_log
def create_recipe(**kwargs):
    user_id = kwargs.get("user_id")
    new_recipe = CreateRecipeSchema(
        name=request.form.get("name"),
        chef_id=request.form.get("chef_id"),
        additional_information=request.form.get("additional_information"),
        ingredients=request.form.getlist("ingredients"),
        preparation_mode=request.form.getlist("preparation_mode"),
        recipe_imgs=request.files.getlist("recipe_imgs"),
    )

    recipe = recipe_controller.create_recipe(user_id, new_recipe)
    return recipe, 201


@recipe_api.route("/<recipe_id>", methods=["PATCH"])
@authentication
@audit_log
def update_recipe(recipe_id, **kwargs):
    user_id = kwargs.get("user_id")
    recipe_data = UpdateRecipeSchema(
        name=request.form.get("name"),
        chef_id=request.form.get("chef_id"),
        additional_information=request.form.get("additional_information"),
        ingredients=request.form.getlist("ingredients"),
        preparation_mode=request.form.getlist("preparation_mode"),
        recipe_imgs=request.files.getlist("recipe_imgs"),
        delete_imgs=request.form.getlist("delete_imgs"),
    )

    recipe = recipe_controller.update_recipe(recipe_id, user_id, recipe_data)

    return recipe, 200


@recipe_api.route("/<recipe_id>", methods=["DELETE"])
@authentication
@audit_log
def delete_recipe(recipe_id, **kwargs):
    user_id = kwargs.get("user_id")

    recipe_controller.delete_recipe(recipe_id, user_id)

    return {}, 204


@recipe_api.route("/<recipe_id>", methods=["GET"])
@authentication
def get_recipe(recipe_id, **kwargs):
    recipe = recipe_controller.get_recipe(recipe_id)

    return recipe, 200


@recipe_api.route("", methods=["GET"])
@authentication
def list_recipe(**kwargs):
    recipes = recipe_controller.list_recipe()

    return recipes, 200
