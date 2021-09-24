from app.ext.api.controller import users_controller
from app.ext.api.decorators import (
    admin_required,
    audit_log,
    authentication,
    user_self_required,
)
from flask import Blueprint, request

user_api = Blueprint("user", __name__)


@user_api.route("", methods=["POST"])
@authentication
@admin_required
@audit_log
def create_user(**kwargs):
    new_user = request.get_json()

    user = users_controller.create_user(new_user)

    return user, 201


@user_api.route("", methods=["GET"])
@authentication
@admin_required
def list_user(**kwargs):
    users = users_controller.list_user()

    return users, 200


@user_api.route("/<id>", methods=["DELETE"])
@authentication
@admin_required
@audit_log
def delete_user(id, **kwargs):
    users_controller.delete_user(id)

    return {}, 204


@user_api.route("/<id>", methods=["GET"])
@authentication
@user_self_required
def get_user(id, **kwargs):
    user = users_controller.get_user(id)

    return user, 200


@user_api.route("<id>", methods=["PATCH"])
@authentication
@user_self_required
@audit_log
def update_user(id, **kwargs):
    user_data = request.json

    user = users_controller.update_user(id, user_data)

    return user, 200


@user_api.route("/confirm/<token>", methods=["GET"])
def confirm_user(token):
    user = users_controller.confirm_user(token)

    return user
