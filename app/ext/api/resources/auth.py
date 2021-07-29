from app.ext.api.controller import auth_controller
from flask import Blueprint, request

auth_api = Blueprint("auth", __name__)


@auth_api.route("/reset", methods=["PATCH"])
def password_reset():
    user = request.get_json()

    user = auth_controller.password_reset(user)

    return user, 202
