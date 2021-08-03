from app.ext.api.controller import users_controller
from app.ext.api.decorators import admin_required, authentication
from flask import Blueprint, request

user_api = Blueprint("user", __name__)


@user_api.route("", methods=["POST"])
@authentication
@admin_required
def create_user(**kwargs):
    new_user = request.get_json()

    user = users_controller.create_user(new_user)

    return user, 201


@user_api.route("/profile", methods=["GET"])
@authentication
def show_profile(**kwargs):
    user_id = kwargs.get("user_id")

    user = users_controller.get_profile_user(user_id)

    return user, 200


@user_api.route("/confirm/<token>", methods=["GET"])
def confirm_user(token):
    user = users_controller.confirm_user(token)

    return user
