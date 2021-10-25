from app.ext.api.controller import chef_controller
from app.ext.api.decorators import admin_required, audit_log, authentication
from app.ext.api.exceptions import InvalidParameters
from app.ext.api.schemas.chef_schemas import CreateChefSchema, UpdateChefSchema
from flask import Blueprint, request
from pydantic import ValidationError

chef_api = Blueprint("chef", __name__)


@chef_api.route("", methods=["POST"])
@authentication
@admin_required
@audit_log
def create_chef(**kwargs):
    try:
        new_chef = CreateChefSchema(
            name=request.form.get("name"), avatar=request.files.get("avatar")
        )
    except ValidationError:
        raise InvalidParameters
    chef = chef_controller.create_chef(new_chef)

    return chef, 201


@chef_api.route("/<chef_id>", methods=["PATCH"])
@authentication
@admin_required
@audit_log
def update_chef(chef_id, **kwargs):
    try:
        chef_data = UpdateChefSchema(
            name=request.form.get("name"), avatar=request.files.get("avatar")
        )
    except ValidationError:
        raise InvalidParameters

    chef = chef_controller.update_chef(chef_id, chef_data)

    return chef, 200


@chef_api.route("/<chef_id>", methods=["DELETE"])
@authentication
@admin_required
@audit_log
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
