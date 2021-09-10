from functools import wraps

from app.ext.api.exceptions import AdminPermissionRequired, InvalidToken
from app.ext.api.services import token_services, users_services
from flask import request
from jwt import (
    ExpiredSignatureError,
    InvalidKeyError,
    InvalidSignatureError,
    InvalidTokenError,
)


def authentication(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            token = request.headers.get("Authorization")

            if not token:
                raise InvalidToken

            user = token_services.verify_token(token)

            kwargs["user_id"] = user.get("user_id")
            kwargs["email"] = user.get("email")

            return f(*args, **kwargs)

        except (
            ExpiredSignatureError,
            InvalidKeyError,
            InvalidSignatureError,
            InvalidTokenError,
        ):
            raise InvalidToken

    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not users_services.is_admin(kwargs.get("user_id")):
            raise AdminPermissionRequired

        return f(*args, **kwargs)

    return decorated_function
