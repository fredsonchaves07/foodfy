from app.ext.api.exceptions import IncorrectLogin, InvalidToken, UserNotFound
from app.ext.api.services import token_services, users_services
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
        user = decode(user_data.token, settings.SECRET_KEY, algorithms=["HS256"])
    except (
        ExpiredSignatureError,
        InvalidKeyError,
        InvalidSignatureError,
        InvalidTokenError,
    ):
        raise InvalidToken

    if not users_services.find_by_id(user.get("user_id")):
        raise UserNotFound

    user = users_services.password_reset(user.get("user_id"), user_data.password)

    return user


def login(user_data):
    email = user_data.email

    user = users_services.find_by_email(email)

    if not user:
        raise IncorrectLogin

    password = user_data.password

    if not users_services.password_match(email, password):
        raise IncorrectLogin

    if not users_services.is_confirmed(user.id):
        users_services.confirm_user(user.id)

    token = token_services.generate_token(user.id, user.email)

    return {"id": user.id, "email": user.email, "token": token}
