from app.ext.api.exceptions import EmailAlreadyExist
from app.ext.api.services import token_services, users_services, util_services


def create_user(new_user):
    name = new_user["name"]
    email = new_user["email"]
    password = new_user["password"]
    admin = new_user["admin"]

    user = users_services.find_by_email(email)

    if user:
        raise EmailAlreadyExist

    user = users_services.create_user(name, email, password, admin)
    token = token_services.generate_token(user["id"], user["email"])

    # TODO -> Url for auth confirmation
    util_services.send_mail(
        user["email"], "Access your account", "mail/confirm.html", token=token
    )

    return user


def confirm_user(user_id):
    if users_services.is_confirmed(user_id):
        return False

    users_services.confirm_user(user_id)

    return True
