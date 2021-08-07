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


@user_api.route("/list", methods=["GET"])
@authentication
@admin_required
def list_user(**kwargs):
    users = users_controller.list_user()

    return users, 200


@user_api.route("/<user_id>", methods=["DELETE"])
@authentication
@admin_required
def delete_user(user_id, **kwargs):
    users_controller.delete_user(user_id)

    return {}, 204


@user_api.route("", methods=["GET"])
@authentication
def get_user(**kwargs):
    user_id = kwargs.get("user_id")

    user = users_controller.get_user(user_id)

    return user, 200


@user_api.route("", methods=["PATCH"])
@authentication
def update_user(**kwargs):
    user_id = kwargs.get("user_id")

    user_data = request.get_json()

    user = users_controller.update_user(user_id, user_data)

    return user, 200


@user_api.route("/confirm/<token>", methods=["GET"])
def confirm_user(token):
    user = users_controller.confirm_user(token)

    return user
