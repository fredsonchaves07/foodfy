from app.ext.api.controller import users_controller
from app.ext.api.decorators import (
    admin_required,
    audit_log,
    authentication,
    user_self_required,
)
from app.ext.api.exceptions import InvalidParameters
from app.ext.api.schemas.user_schemas import CreateUserSchema, UpdateUserSchema
from flask import Blueprint, request
from pydantic import ValidationError

user_api = Blueprint("user", __name__)


@user_api.route("", methods=["POST"])
@authentication
@admin_required
@audit_log
def create_user(**kwargs):
    """
    user creation endpoint
    ---
    tags:
      - User
    parameters:
      - name: user
        in: body
        required: true
        description:
          User creation endpoint
        schema:
          id: User
          properties:
            name:
              type: string
              example: "Teste"
            email:
              type: string
              example: "Teste@email.com"
            password:
              type: string
              example: "1234"
            admin:
              type: boolean
              example: false
    responses:
      201:
        description: User created successfully
      400:
        description: Invalid parameters in request
      401:
        description: Operation not allowed. Consult the administrator
      422:
        description: Email already exist
      498:
        description: Expired or invalid token.
    """
    try:
        new_user = CreateUserSchema(**request.get_json())
    except ValidationError:
        raise InvalidParameters

    user = users_controller.create_user(new_user)

    return user, 201


@user_api.route("", methods=["GET"])
@authentication
@admin_required
def list_user(**kwargs):
    """
    user list endpoint
    ---
    tags:
      - User
    responses:
      200:
        description: User created successfully
        schema:
          $ref: '#/definitions/User'
      401:
        description: Operation not allowed. Consult the administrator
      498:
        description: Expired or invalid token.
    """
    users = users_controller.list_user()

    return users, 200


@user_api.route("/<id>", methods=["DELETE"])
@authentication
@admin_required
@audit_log
def delete_user(id, **kwargs):
    """
    user delete endpoint
    ---
    tags:
      - User
    parameters:
      - name: id
        in: path
        required: true
        type: string
        description:
          User id
        schema:
          id: User
          properties:
            name:
              type: string
              example: "Teste"
            email:
              type: string
              example: "Teste@email.com"
            password:
              type: string
              example: "1234"
            admin:
              type: boolean
              example: false
    responses:
      200:
        description: User created successfully
        schema:
          $ref: '#/definitions/User'
      401:
        description: Operation not allowed. Consult the administrator
      404:
        description: User not found
      498:
        description: Expired or invalid token.
    """
    users_controller.delete_user(id)

    return {}, 204


@user_api.route("/<id>", methods=["GET"])
@authentication
@user_self_required
def get_user(id, **kwargs):
    """
    user get endpoint
    ---
    tags:
      - User
    parameters:
      - name: id
        in: path
        required: true
        type: string
        description:
          User id
        schema:
          id: User
          properties:
            name:
              type: string
              example: "Teste"
            email:
              type: string
              example: "Teste@email.com"
            password:
              type: string
              example: "1234"
            admin:
              type: boolean
              example: false
    responses:
      200:
        description: User created successfully
        schema:
          $ref: '#/definitions/User'
      401:
        description: Operation not allowed. Consult the administrator
      404:
        description: User not found
      498:
        description: Expired or invalid token.
    """
    user = users_controller.get_user(id)

    return user, 200


@user_api.route("<id>", methods=["PATCH"])
@authentication
@user_self_required
@audit_log
def update_user(id, **kwargs):
    """
    user update endpoint
    ---
    tags:
      - User
    parameters:
      - name: id
        in: path
        required: true
        type: string
        description:
          User id
      - name: user data
        in: body
        schema:
          id: User
          properties:
            name:
              type: string
              example: "Teste"
            email:
              type: string
              example: "Teste@email.com"
            password:
              type: string
              example: "1234"
            admin:
              type: boolean
              example: false
    responses:
      200:
        description: User created successfully
      400:
        description: Invalid parameters in request
      401:
        description: Operation not allowed. Consult the administrator
      404:
        description: User not found
      422:
        description: Email already exist
      498:
        description: Expired or invalid token.
    """
    try:
        user_data = UpdateUserSchema(**request.get_json())
    except ValidationError:
        raise InvalidParameters

    user = users_controller.update_user(id, user_data)

    return user, 200


@user_api.route("/confirm/<token>", methods=["GET"])
def confirm_user(token):
    user = users_controller.confirm_user(token)

    return user
