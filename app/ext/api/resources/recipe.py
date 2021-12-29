from app.ext.api.controller import recipe_controller
from app.ext.api.decorators import audit_log, authentication
from app.ext.api.exceptions import InvalidParameters
from app.ext.api.schemas.recipe_schemas import CreateRecipeSchema, UpdateRecipeSchema
from flask import Blueprint, request
from pydantic import ValidationError

recipe_api = Blueprint("recipe", __name__)


@recipe_api.route("", methods=["POST"])
@authentication
@audit_log
def create_recipe(**kwargs):
    """
    recipe creation endpoint
    ---
    tags:
      - Recipe
    parameters:
      - name: recipe data
        in: body
        required: true
        description:
          Recipe body data
        schema:
          id: Recipe
          required:
            - name
            - ingredients
            - preparation_mode
            - chef_id
            - recipe_imgs
          properties:
            name:
              name: string
              example: "Teste"
            ingredients:
              type: array
              example: ["ingredient1", "ingredient1"]
            preparation_mode:
              type: array
              example: ["preparation1", "preparation2"]
            chef_id:
              type: string
              example: "a120c8a9v10"
            additional_information:
              type: string
              example: "recipe additional information"
            recipe_imgs:
              type: array
              example: ["recipe_img1", "recipe_img2"]
    responses:
      201:
        description: Recipe created successfully
      400:
        description: Invalid parameters in request
      400:
        description: Maximum image capacity reached. Check the required quantity
      404:
        description: Chef not found
      498:
        description: Expired or invalid token.
    """
    user_id = kwargs.get("user_id")
    try:
        new_recipe = CreateRecipeSchema(
            name=request.form.get("name"),
            chef_id=request.form.get("chef_id"),
            additional_information=request.form.get("additional_information"),
            ingredients=request.form.getlist("ingredients"),
            preparation_mode=request.form.getlist("preparation_mode"),
            recipe_imgs=request.files.getlist("recipe_imgs"),
        )
    except ValidationError:
        raise InvalidParameters
    recipe = recipe_controller.create_recipe(user_id, new_recipe)
    return recipe, 201


@recipe_api.route("/<recipe_id>", methods=["PATCH"])
@authentication
@audit_log
def update_recipe(recipe_id, **kwargs):
    """
    recipe update endpoint
    ---
    tags:
      - Recipe
    parameters:
      - name: redipe id
        in: path
        required: true
      - name: recipe data
        in: body
        required: false
        description:
          Recipe body data
        schema:
          id: Recipe
          required:
            - name
            - ingredients
            - preparation_mode
            - chef_id
            - recipe_imgs
          properties:
            name:
              name: string
              example: "Teste"
            ingredients:
              type: array
              example: ["ingredient1", "ingredient1"]
            preparation_mode:
              type: array
              example: ["preparation1", "preparation2"]
            chef_id:
              type: string
              example: "a120c8a9v10"
            additional_information:
              type: string
              example: "recipe additional information"
            recipe_imgs:
              type: array
              example: ["recipe_img1", "recipe_img2"]
    responses:
      200:
        description: Recipe updated successfully
      400:
        description: Invalid parameters in request
      400:
        description: Maximum image capacity reached. Check the required quantity
      401:
        description: Operation not allowed. Consult the administrator
      404:
        description: Recipe not found
      404:
        description: Chef not found
      498:
        description: Expired or invalid token.
    """
    user_id = kwargs.get("user_id")
    try:
        recipe_data = UpdateRecipeSchema(
            name=request.form.get("name"),
            chef_id=request.form.get("chef_id"),
            additional_information=request.form.get("additional_information"),
            ingredients=request.form.getlist("ingredients"),
            preparation_mode=request.form.getlist("preparation_mode"),
            recipe_imgs=request.files.getlist("recipe_imgs"),
            delete_imgs=request.form.getlist("delete_imgs"),
        )
    except ValidationError:
        raise InvalidParameters
    recipe = recipe_controller.update_recipe(recipe_id, user_id, recipe_data)

    return recipe, 200


@recipe_api.route("/<recipe_id>", methods=["DELETE"])
@authentication
@audit_log
def delete_recipe(recipe_id, **kwargs):
    """
    recipe delete endpoint
    ---
    tags:
      - Recipe
    parameters:
      - name: redipe id
        in: path
        required: true
    responses:
      204:
        description: Recipe deleted successfully
      400:
        description: Invalid parameters in request
      401:
        description: Operation not allowed. Consult the administrator
      404:
        description: Recipe not found
      498:
        description: Expired or invalid token.
    """
    user_id = kwargs.get("user_id")

    recipe_controller.delete_recipe(recipe_id, user_id)

    return {}, 204


@recipe_api.route("/<recipe_id>", methods=["GET"])
@authentication
def get_recipe(recipe_id, **kwargs):
    """
    recipe get endpoint
    ---
    tags:
      - Recipe
    parameters:
      - name: redipe id
        in: path
        required: true
    responses:
      200:
        description: OK
        schema:
          $ref: '#/definitions/Recipe'
      404:
        description: Recipe not found
      498:
        description: Expired or invalid token.
    """
    recipe = recipe_controller.get_recipe(recipe_id)

    return recipe, 200


@recipe_api.route("", methods=["GET"])
@authentication
def list_recipe(**kwargs):
    """
    recipe get endpoint
    ---
    tags:
      - Recipe
    responses:
      200:
        description: OK
        schema:
          $ref: '#/definitions/Recipe'
      498:
        description: Expired or invalid token.
    """
    recipes = recipe_controller.list_recipe()

    return recipes, 200
