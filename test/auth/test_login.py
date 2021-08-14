import json

from app.ext.api.controller import users_controller
from app.ext.api.exceptions import UserNotFound


def test_login(client, database):
    new_user = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    users_controller.create_user(new_user)

    user_data = {"email": new_user.get("email"), "password": new_user.get("password")}
    headers = {"content-type": "application/json"}

    response = client.post(
        "/api/v1/auth/login", data=json.dumps(user_data), headers=headers
    )

    assert response.content_type == "application/json"
    assert response.status_code == 200
    assert response.json["email"] == new_user.get("email")
    assert response.json["id"]
    assert response.json["token"]


def test_no_login_with_email_no_already_exist(client, database):
    new_user = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    users_controller.create_user(new_user)

    user_data = {"email": "noexist@email.com", "password": new_user.get("password")}
    headers = {"content-type": "application/json"}

    response = client.post(
        "/api/v1/auth/login", data=json.dumps(user_data), headers=headers
    )

    assert response.status_code == UserNotFound.code
    assert response.json["message"] == UserNotFound.message


def test_no_login_with_wrong_password(client, database):
    new_user = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    users_controller.create_user(new_user)

    user_data = {"email": new_user.get("email"), "password": "3512"}
    headers = {"content-type": "application/json"}

    response = client.post(
        "/api/v1/auth/login", data=json.dumps(user_data), headers=headers
    )

    assert response.status_code == UserNotFound.code
    assert response.json["message"] == UserNotFound.message
