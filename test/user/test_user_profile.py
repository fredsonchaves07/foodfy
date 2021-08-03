from app.ext.api.controller import users_controller
from app.ext.api.exceptions import UserNotFound
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
