import json

from app.ext.api.controller import users_controller
from app.ext.api.exceptions import EmailAlreadyExist, OperationNotAllowed, UserNotFound
from app.ext.api.services import token_services


def test_show_profile(database, client):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(new_user1)
    user_id = user.get("id")
    token = token_services.generate_token(user.get("id"), user.get("email"))

    headers = {"Authorization": token}

    response = client.get(f"/api/v1/user/{user_id}", headers=headers)

    assert response.content_type == "application/json"
    assert response.status_code == 200
    assert response.json["email"] == new_user1["email"]
    assert response.json["name"] == new_user1["name"]


def test_no_show_profile_user_if_user_not_exist(admin_user, client):
    headers = {"Authorization": admin_user.get("token")}

    response = client.get("/api/v1/user/105542", headers=headers)

    assert response.status_code == UserNotFound.code
    assert response.json["message"] == UserNotFound.message


def test_update_profile_name(client, database):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(new_user1)
    user_id = user.get("id")
    token = token_services.generate_token(user.get("id"), user.get("email"))

    update_user = {"name": "Usuário teste2"}

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    response = client.patch(
        f"/api/v1/user/{user_id}", headers=headers, data=json.dumps(update_user)
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
    user_id = user.get("id")
    token = token_services.generate_token(user.get("id"), user.get("email"))

    update_user = {"name": "Usuário teste2", "password": "54321"}

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    response = client.patch(
        f"/api/v1/user/{user_id}", headers=headers, data=json.dumps(update_user)
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
    user_id = user.get("id")
    token = token_services.generate_token(user.get("id"), user.get("email"))

    update_user = {"email": "email1@email.com"}

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    response = client.patch(
        f"/api/v1/user/{user_id}", headers=headers, data=json.dumps(update_user)
    )

    assert response.content_type == "application/json"
    assert response.json["email"] == update_user.get("email")
    assert response.status_code == 200


def test_profile_user_is_admin(admin_user, client):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(new_user1)
    user_id = user.get("id")

    update_user = {"admin": True}

    headers = {
        "Authorization": admin_user.get("token"),
        "content-type": "application/json",
    }

    response = client.patch(
        f"/api/v1/user/{user_id}", headers=headers, data=json.dumps(update_user)
    )

    assert response.content_type == "application/json"
    assert response.json["is_admin"] == update_user.get("admin")
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
    user_id = user.get("id")
    token = token_services.generate_token(user.get("id"), user.get("email"))

    update_user = {"email": "email1@email.com"}

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    response = client.patch(
        f"/api/v1/user/{user_id}", headers=headers, data=json.dumps(update_user)
    )

    assert response.content_type == "application/json"
    assert response.status_code == EmailAlreadyExist.code
    assert response.json["message"] == EmailAlreadyExist.message


def test_not_update_profile_if_user_not_already_exist(client, admin_user):
    update_user = {"name": "user2"}

    headers = {"Authorization": admin_user.get("token")}

    response = client.patch(
        "/api/v1/user/100", headers=headers, data=json.dumps(update_user)
    )

    assert response.status_code == UserNotFound.code
    assert response.json["message"] == UserNotFound.message


def test_not_turn_admin_user_if_user_is_not_admin(client, database):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(new_user1)
    user_id = user.get("id")
    token = token_services.generate_token(user.get("id"), user.get("email"))

    update_user = {"admin": True}

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    response = client.patch(
        f"/api/v1/user/{user_id}", headers=headers, data=json.dumps(update_user)
    )

    assert response.content_type == "application/json"
    assert response.status_code == OperationNotAllowed.code
    assert response.json["message"] == OperationNotAllowed.message


def test_delete_user(client, admin_user):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(new_user1)

    headers = {
        "Authorization": admin_user.get("token"),
        "content-type": "application/json",
    }

    response = client.delete(
        f"/api/v1/user/{user.get('id')}",
        headers=headers,
    )

    assert response.content_type == "application/json"
    assert response.status_code == 204
