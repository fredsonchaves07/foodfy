import json

from app.ext.api.controller import users_controller
from app.ext.api.exceptions import (
    AdminPermissionRequired,
    EmailAlreadyExist,
    InvalidToken,
    InvalidUser,
    UserNotFound,
)
from app.ext.api.services import token_services


def test_create_user(client, database, admin_user):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    headers = {
        "Authorization": admin_user.get("token"),
        "content-type": "application/json",
    }

    response = client.post(
        "/api/v1/user",
        data=json.dumps(new_user1),
        headers=headers,
    )

    assert response.content_type == "application/json"
    assert response.json["email"] == new_user1["email"]
    assert response.status_code == 201


def test_no_create_user_with_email_already_exist(client, database, admin_user):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    headers = {
        "Authorization": admin_user.get("token"),
        "content-type": "application/json",
    }

    client.post(
        "/api/v1/user",
        data=json.dumps(new_user1),
        headers=headers,
    )

    new_user2 = {
        "name": "Usuário teste2",
        "email": "email@email.com",
        "password": "123416",
        "admin": False,
    }

    response = client.post("/api/v1/user", data=json.dumps(new_user2), headers=headers)

    assert response.status_code == EmailAlreadyExist.code
    assert response.json["message"] == EmailAlreadyExist.message


def test_no_create_user_not_an_administrator(client, database):
    token = token_services.generate_token("10", "false_admin@email.com")

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    response = client.post("/api/v1/user", data=json.dumps(new_user1), headers=headers)

    assert response == AdminPermissionRequired.code
    assert response.json["message"] == AdminPermissionRequired.message


def test_confirm_user(client, database):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(new_user1)

    token = token_services.generate_token(user.get("id"), user.get("email"))

    response = client.get(f"/api/v1/user/confirm/{token}")

    assert response.content_type == "application/json"
    assert response.json["email"] == new_user1["email"]
    assert response.status_code == 200


def test_no_confirm_user_if_user_already_confirmed(client, database):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(new_user1)

    token = token_services.generate_token(user.get("id"), user.get("email"))

    client.get(f"/api/v1/user/confirm/{token}")

    response = client.get(f"/api/v1/user/confirm/{token}")

    assert response.status_code == InvalidUser.code
    assert response.json["message"] == InvalidUser.message


def test_no_confirm_user_if_user_not_found(client, database):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    token = token_services.generate_token(new_user1.get("id"), new_user1.get("email"))

    response = client.get(f"/api/v1/user/confirm/{token}")

    assert response.status_code == UserNotFound.code
    assert response.json["message"] == UserNotFound.message


def test_no_confirm_user_if_token_is_invalid(client, database):
    response = client.get("/api/v1/user/confirm/105021054ascfr9")

    assert response.status_code == InvalidToken.code
    assert response.json["message"] == InvalidToken.message
