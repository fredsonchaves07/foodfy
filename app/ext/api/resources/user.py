from app.ext.api.controller import users_controller
from app.ext.api.decorators import authentication
from flask import Blueprint, request

user_api = Blueprint("user", __name__)


@user_api.route("", methods=["POST"])
@authentication
def create_user(**kwargs):
    new_user = request.get_json()

    user = users_controller.create_user(new_user)

    return user


@user_api.route("/confirm", methods=["POST"])
def confirm_user(**kwargs):
    # token = request.form.get("token")
    # users_controller.confirm_user()
    return "ok", 200
