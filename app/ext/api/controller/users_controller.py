from app.ext.api.controller import recipe_controller
from app.ext.api.exceptions import (
    EmailAlreadyExist,
    InvalidToken,
    InvalidUser,
    UserNotFound,
)
from app.ext.api.services import token_services, users_services, util_services
from dynaconf import settings
from flask import session


def create_user(new_user):
    name = new_user.name
    email = new_user.email
    password = new_user.password
    admin = new_user.admin

    user = users_services.find_by_email(email)

    if user:
        raise EmailAlreadyExist

    user = users_services.create_user(name, email, password, admin)
    token = token_services.generate_token(user["id"], user["email"])  # noqa

    if settings.SEND_MAIL:
        util_services.send_mail(
            user["email"],
            "Access your account",
            "mail/confirm.html",
            token=token,
            confirm_url=settings.CONFIRM_USER_URL,
        )

    session["audit_log"] = {
        "object_type": "USER",
        "object_id": user.get("id"),
        "object_name": user.get("name"),
        "action": "CREATE",
    }

    return user


def confirm_user(token):
    try:
        user = token_services.verify_token(token)
    except Exception:
        raise InvalidToken

    if users_services.is_confirmed(user.get("user_id")):
        raise InvalidUser

    user = users_services.confirm_user(user.get("user_id"))

    if not user:
        raise UserNotFound

    return user


def list_user():
    users = users_services.list_user()

    return {"users": users}


def get_user(user_id):
    user = users_services.find_by_id(user_id)

    if not user:
        raise UserNotFound

    return {
        "user_id": user.id,
        "name": user.name,
        "email": user.email,
        "is_admin": user.is_admin,
    }


def update_user(user_id, user_data):
    user = users_services.find_by_id(user_id)

    if not user:
        raise UserNotFound

    email = user_data.email

    if users_services.find_by_email(email):
        raise EmailAlreadyExist

    password = user_data.password
    name = user_data.name
    admin = user_data.admin

    user = users_services.update_user(user_id, email, password, name, admin)

    session["audit_log"] = {
        "object_type": "USER",
        "object_id": user.id,
        "object_name": user.name,
        "action": "UPDATE",
    }

    return {
        "user_id": user.id,
        "name": user.name,
        "email": user.email,
        "is_admin": user.is_admin,
    }


def delete_user(user_id):
    user = users_services.find_by_id(user_id)

    if not user:
        UserNotFound

    for recipe in user.recipes:
        recipe_controller.delete_recipe(recipe.id, user_id)

    session["audit_log"] = {
        "object_type": "USER",
        "object_id": user.id,
        "object_name": user.name,
        "action": "DELETE",
    }

    users_services.delete_user(user_id)
