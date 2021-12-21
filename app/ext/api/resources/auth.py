from app.ext.api.controller import auth_controller
from app.ext.api.exceptions import InvalidParameters
from app.ext.api.schemas.auth_schemas import LoginSchema, ResetPasswordSchema
from flask import Blueprint, request
from pydantic import ValidationError

auth_api = Blueprint("auth", __name__)


@auth_api.route("/reset", methods=["PATCH"])
def password_reset():
    try:
        user_data = ResetPasswordSchema(**request.get_json())
    except ValidationError:
        raise InvalidParameters
    user = auth_controller.password_reset(user_data)

    return user, 200


@auth_api.route("/login", methods=["POST"])
def login():
    """
    authentication endpoint
    ---
    tags:
      - login
    parameters:
      - name: login
        in: body
        required: true
        description:
          User authentication
        schema:
          id: Login
          required:
            - email
            - password
          properties:
            email:
              type: string
              example: "email@email.com"
            password:
              type: string
              example: "1234"
    responses:
      200:
        description: Authenticated successfuly
      400:
        description: Invalid parameters in request
      401:
        description: Data access incorrect
    """
    try:
        user_data = LoginSchema(**request.get_json())
    except ValidationError:
        raise InvalidParameters

    auth_data = auth_controller.login(user_data)

    return auth_data, 200
