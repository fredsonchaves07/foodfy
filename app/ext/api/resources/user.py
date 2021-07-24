# from app.ext.api.controller import users_controller
from flask import Blueprint

user_api = Blueprint("user", __name__)


@user_api.route("", methods=["POST"])
def create_user(**kwargs):
    # users_controller.create_user()
    return "ok", 201


@user_api.route("/confirm", methods=["POST"])
def confirm_user(**kwargs):
    # token = request.form.get("token")
    # users_controller.confirm_user()
    return "ok", 200
