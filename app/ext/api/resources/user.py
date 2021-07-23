from app.ext.api.controller import users_controller
from flask import Blueprint

user_api = Blueprint("user", __name__)


@user_api.route("", methods=["POST"])
def create_user():
    users_controller.create_user()
    return "ok", 201
