from app.ext.api.controller import auth_controller
from app.ext.api.exceptions import InvalidParameters
from app.ext.api.schemas.auth_schemas import LoginSchema
from flask import Blueprint, request
from pydantic import ValidationError

auth_api = Blueprint("auth", __name__)


@auth_api.route("/reset", methods=["PATCH"])
def password_reset():
    user_data = request.get_json()

    user = auth_controller.password_reset(user_data)

    return user, 200


@auth_api.route("/login", methods=["POST"])
def login():
    try:
        user_data = LoginSchema(**request.get_json())
    except ValidationError:
        raise InvalidParameters

    auth_data = auth_controller.login(user_data)

    return auth_data, 200
