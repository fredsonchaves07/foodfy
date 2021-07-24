from dynaconf import settings
from jwt import encode


def generate_confirm_token(user_id, email, expiration=3600):
    token = encode(
        {"user_id": user_id, "email": email, "exp": expiration}, settings.SECRET_KEY
    )

    return token
