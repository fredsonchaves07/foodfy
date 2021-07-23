from flask import Blueprint

user_api = Blueprint("user", __name__)


@user_api.route("", methods=["POST"])
def create_user():
    return "ok", 201
