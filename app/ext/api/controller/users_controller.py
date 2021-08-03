from app.ext.api.exceptions import EmailAlreadyExist, InvalidUser, UserNotFound
from app.ext.api.services import token_services, users_services, util_services  # noqa


def create_user(new_user):
    name = new_user["name"]
    email = new_user["email"]
    password = new_user["password"]
    admin = new_user["admin"]

    user = users_services.find_by_email(email)

    if user:
        raise EmailAlreadyExist

    user = users_services.create_user(name, email, password, admin)
    token = token_services.generate_token(user["id"], user["email"])  # noqa

    # util_services.send_mail(
    #     user["email"], "Access your account", "mail/confirm.html", token=token
    # )

    return user


def confirm_user(token):
    user = token_services.verify_token(token)

    if users_services.is_confirmed(user.get("user_id")):
        raise InvalidUser

    user = users_services.confirm_user(user.get("user_id"))

    if not user:
        raise UserNotFound

    return user


def get_profile_user(user_id):
    user = users_services.find_by_id(user_id)

    if not user:
        raise UserNotFound

    return {
        "user_id": user.id,
        "name": user.name,
        "email": user.email,
        "is_admin": user.is_admin,
    }
