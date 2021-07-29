from datetime import datetime, timedelta

from dynaconf import settings
from jwt import decode, encode


def generate_token(user_id, email):
    token = encode(
        {
            "user_id": user_id,
            "email": email,
            "exp": datetime.utcnow() + timedelta(hours=1),
        },
        settings.SECRET_KEY,
    )

    return token


def verify_token(token):
    user = decode(token, settings.SECRET_KEY, algorithms=["HS256"])

    return user
