from app.ext.api.controller import users_controller
from app.ext.api.exceptions import AdminPermissionRequired
from app.ext.api.services import token_services


def test_list_users(client, admin_user):

    users = [
        {
            "name": "Usuário 1",
            "email": "email1@email.com",
            "password": "123456",
            "admin": False,
        },
        {
            "name": "Usuário 2",
            "email": "email2@email.com",
            "password": "123456",
            "admin": False,
        },
        {
            "name": "Usuário 3",
            "email": "email3@email.com",
            "password": "123456",
            "admin": False,
        },
    ]

    for user in users:
        users_controller.create_user(user)

    headers = {
        "Authorization": admin_user.get("token"),
        "content-type": "application/json",
    }

    response = client.get(
        "/api/v1/user/list",
        headers=headers,
    )

    assert response.content_type == "application/json"
    assert response.status_code == 200
    assert len(response.json["users"]) >= len(users)


def test_no_list_user_if_user_is_not_admin(client, database):
    user1 = {
        "name": "Usuário 1",
        "email": "email1@email.com",
        "password": "123456",
        "admin": False,
    }

    user = users_controller.create_user(user1)
    token = token_services.generate_token(user.get("id"), user.get("email"))

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    response = client.get("/api/v1/user/list", headers=headers)

    assert response.status_code == AdminPermissionRequired.code
    assert response.json["message"] == AdminPermissionRequired.message
