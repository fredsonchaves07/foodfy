from functools import wraps

from app.ext.api.exceptions import (
    AdminPermissionRequired,
    InvalidToken,
    OperationNotAllowed,
)
from app.ext.api.services import audit_log_services, token_services, users_services
from flask import request, session
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


def user_self_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user = kwargs.get("user_id")
        update_user = kwargs.get("id")
        admin = request.json.get("admin") if request.json else None

        if current_user != update_user and not users_services.is_admin(current_user):
            raise OperationNotAllowed

        if admin and not users_services.is_admin(current_user):
            raise OperationNotAllowed

        return f(*args, **kwargs)

    return decorated_function


def audit_log(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response = f(*args, **kwargs)

        session["audit_log"].update({"done_by": kwargs.get("email")})

        audit_log = session["audit_log"]

        audit_log_services.create_audit(audit_log)

        return response

    return decorated_function
