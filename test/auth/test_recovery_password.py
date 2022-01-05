import json

from app.ext.api.controller import users_controller
from app.ext.api.exceptions import InvalidParameters, InvalidToken, UserNotFound
from app.ext.api.schemas.user_schemas import CreateUserSchema
from app.ext.api.services import token_services


def test_recovery_password(client, database):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(CreateUserSchema(**new_user1))
    token = token_services.generate_token(user.get("id"), user.get("email"))
    user_data = {"token": token, "password": "1234"}
    headers = {"content-type": "application/json"}

    response = client.patch(
        "/api/v1/auth/reset", data=json.dumps(user_data), headers=headers
    )

    assert response.content_type == "application/json"
    assert response.status_code == 200
    assert response.json["email"] == new_user1.get("email")


def test_no_recovery_password_if_user_not_already_exist(client, database):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    token = token_services.generate_token("10", new_user1.get("email"))
    user_data = {"token": token, "password": "1234"}
    headers = {"content-type": "application/json"}

    response = client.patch(
        "/api/v1/auth/reset", data=json.dumps(user_data), headers=headers
    )

    assert response.status_code == UserNotFound.code
    assert response.json["message"] == UserNotFound.message


def test_no_recovery_password_with_invalid_token(client, database):
    user_data = {"token": "asas100c547896210", "password": "1234"}
    headers = {"content-type": "application/json"}

    response = client.patch(
        "/api/v1/auth/reset", data=json.dumps(user_data), headers=headers
    )

    assert response.status_code == InvalidToken.code
    assert response.json["message"] == InvalidToken.message


def test_no_recovery_password_with_invalid_params(client, database):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(CreateUserSchema(**new_user1))
    token = token_services.generate_token(user.get("id"), user.get("email"))
    user_data = {"token": token}
    headers = {"content-type": "application/json"}

    response = client.patch(
        "/api/v1/auth/reset", data=json.dumps(user_data), headers=headers
    )

    assert response.status_code == InvalidParameters.code
    assert response.json["message"] == InvalidParameters.message
