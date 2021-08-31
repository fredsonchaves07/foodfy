from app.ext.api.controller import recipe_controller
from app.ext.api.decorators import authentication
from flask import Blueprint, request

recipe_api = Blueprint("recipe", __name__)


@recipe_api.route("", methods=["POST"])
@authentication
def create_recipe(**kwargs):
    user_id = kwargs.get("user_id")
    new_recipe = request.form
    recipe_imgs = request.files.getlist("recipe_imgs")

    recipe = recipe_controller.create_recipe(user_id, new_recipe, recipe_imgs)
    return recipe, 201


@recipe_api.route("/<recipe_id>", methods=["PATCH"])
@authentication
def update_recipe(recipe_id, **kwargs):
    user_id = kwargs.get("user_id")
    recipe_data = request.form
    recipe_imgs = request.files.getlist("recipe_imgs")

    recipe = recipe_controller.update_recipe(
        recipe_id, user_id, recipe_data, recipe_imgs
    )

    return recipe, 200


@recipe_api.route("/<recipe_id>", methods=["DELETE"])
@authentication
def delete_recipe(recipe_id, **kwargs):
    user_id = kwargs.get("user_id")

    recipe_controller.delete_recipe(recipe_id, user_id)

    return {}, 204
