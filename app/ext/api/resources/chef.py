from app.ext.api.controller import chef_controller
from app.ext.api.decorators import admin_required, authentication
from flask import Blueprint, request

chef_api = Blueprint("chef", __name__)


@chef_api.route("", methods=["POST"])
@authentication
@admin_required
def create_chef(**kwargs):
    new_chef = request.form
    avatar_file = request.files.get("avatar")

    chef = chef_controller.create_chef(new_chef, avatar_file)

    return chef, 201


@chef_api.route("/<chef_id>", methods=["PATCH"])
@authentication
@admin_required
def update_chef(chef_id, **kwargs):
    chef_data = request.form
    avatar_file = request.files.get("avatar")

    chef = chef_controller.update_chef(chef_id, chef_data, avatar_file)

    return chef, 200


@chef_api.route("/<chef_id>", methods=["DELETE"])
@authentication
@admin_required
def delete_chef(chef_id, **kwargs):
    chef_controller.delete_chef(chef_id)

    return {}, 204


@chef_api.route("/<chef_id>", methods=["GET"])
@authentication
def get_chef(chef_id, **kwargs):
    chef = chef_controller.get_chef(chef_id)

    return chef, 200


@chef_api.route("", methods=["GET"])
@authentication
def list_chef(**kwargs):
    chefs = chef_controller.list_chef()

    return chefs, 200
