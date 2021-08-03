import json

from app.ext.api.controller import users_controller
from app.ext.api.exceptions import EmailAlreadyExist, UserNotFound
from app.ext.api.services import token_services


def test_show_profile(database, client):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(new_user1)
    token = token_services.generate_token(user.get("id"), user.get("email"))

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    response = client.get(
        "/api/v1/user/profile",
        headers=headers,
    )

    assert response.content_type == "application/json"
    assert response.json["email"] == new_user1["email"]
    assert response.json["name"] == new_user1["name"]
    assert response.status_code == 200


def test_no_show_profile_user_if_user_not_exist(database, client):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(new_user1)
    token = token_services.generate_token("10", user.get("email"))

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    try:
        client.get(
            "/api/v1/user/profile",
            headers=headers,
        )
    except UserNotFound:
        return True


def test_update_profile_name(client, database):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(new_user1)
    token = token_services.generate_token(user.get("id"), user.get("email"))

    update_user = {"name": "Usuário teste2"}

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    response = client.patch(
        "/api/v1/user/profile", headers=headers, data=json.dumps(update_user)
    )

    assert response.content_type == "application/json"
    assert response.json["name"] == update_user.get("name")
    assert response.status_code == 200


def test_update_profile_password(client, database):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(new_user1)
    token = token_services.generate_token(user.get("id"), user.get("email"))

    update_user = {"name": "Usuário teste2", "password": "54321"}

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    response = client.patch(
        "/api/v1/user/profile", headers=headers, data=json.dumps(update_user)
    )

    user_data = {
        "email": new_user1.get("email"),
        "password": update_user.get("password"),
    }

    response2 = client.post(
        "/api/v1/auth/login", headers=headers, data=json.dumps(user_data)
    )

    assert response.content_type == "application/json"
    assert response2.content_type == "application/json"
    assert response.json["name"] == update_user.get("name")
    assert response2.status_code == 200
    assert response.status_code == 200


def test_update_profile_email(client, database):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(new_user1)
    token = token_services.generate_token(user.get("id"), user.get("email"))

    update_user = {"email": "email1@email.com"}

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    response = client.patch(
        "/api/v1/user/profile", headers=headers, data=json.dumps(update_user)
    )

    assert response.content_type == "application/json"
    assert response.json["email"] == update_user.get("email")
    assert response.status_code == 200


def test_not_update_profile_if_email_already_exist(client, database):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    new_user2 = {
        "name": "Usuário teste",
        "email": "email1@email.com",
        "password": "123456",
        "admin": False,
    }

    users_controller.create_user(new_user2)
    user = users_controller.create_user(new_user1)
    token = token_services.generate_token(user.get("id"), user.get("email"))

    update_user = {"email": "email1@email.com"}

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    try:
        client.patch(
            "/api/v1/user/profile", headers=headers, data=json.dumps(update_user)
        )
    except EmailAlreadyExist:
        return True


def test_not_update_profile_if_user_not_already_exist(client, database):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(new_user1)
    token = token_services.generate_token("10", user.get("email"))

    update_user = {"name": "user2"}

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    try:
        client.patch(
            "/api/v1/user/profile", headers=headers, data=json.dumps(update_user)
        )
    except UserNotFound:
        return True
