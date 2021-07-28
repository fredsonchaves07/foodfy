from app.ext.api.exceptions import UserNotFound
from app.ext.api.services import users_services
from dynaconf import settings
from jwt import (
    ExpiredSignatureError,
    InvalidKeyError,
    InvalidSignatureError,
    InvalidTokenError,
    decode,
)


def password_reset(user_data):
    try:
        user = decode(user_data["token"], settings.SECRET_KEY, algorithms=["HS256"])
    except (
        ExpiredSignatureError,
        InvalidKeyError,
        InvalidSignatureError,
        InvalidTokenError,
    ):
        raise InvalidTokenError

    if not users_services.find_by_id(user.get("user_id")):
        raise UserNotFound

    user = users_services.password_reset(user.get("user_id"), user_data.get("password"))

    return user
