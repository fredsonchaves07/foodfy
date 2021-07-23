from app.ext.api.exceptions import AdminPermissionRequired, EmailAlreadyExist
from app.ext.api.services import users_services


# TODO -> Generate password token
# TODO -> Create the email sending service
# TODO -> Sending the user's token created to the registered email
def create_user(new_user, admin):
    if not admin:
        raise AdminPermissionRequired

    name = new_user["name"]
    email = new_user["email"]
    password = new_user["password"]

    user = users_services.find_by_email(email)

    if user:
        raise EmailAlreadyExist

    return users_services.create_user(name, email, password)
