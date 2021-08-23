from app.ext.api.controller import recipe_controller
from app.ext.api.decorators import authentication
from flask import Blueprint, request

recipe_api = Blueprint("recipe", __name__)


@recipe_api.route("", methods=["POST"])
@authentication
def create_recipe(**kwargs):
    new_recipe = request.form
    recipe_imgs = request.files.getlist("recipe_imgs")

    recipe = recipe_controller.create_recipe(new_recipe, recipe_imgs)
    return recipe, 201
