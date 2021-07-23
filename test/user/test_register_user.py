from app.ext.api.controller import users_controller
from app.ext.api.exceptions import AdminPermissionRequired, EmailAlreadyExist


def test_valid_post_request(client):
    assert client.post("/api/v1/user").status_code == 201


def test_create_user(app, database):
    new_user = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "12346",
    }

    user = users_controller.create_user(new_user, "admin@email.com")

    assert user["id"], "Unable to create user"


def test_no_create_user_if_email_already_exist(app, database):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "12346",
    }

    users_controller.create_user(new_user1, "admin@email.com")

    new_user2 = {
        "name": "Usuário teste2",
        "email": "email@email.com",
        "password": "12564",
    }

    try:
        users_controller.create_user(new_user2, "admin@email.com")
    except EmailAlreadyExist:
        assert True
        assert EmailAlreadyExist.code == 422


def test_no_create_user_if_not_admin(app, database):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "12346",
    }

    try:
        users_controller.create_user(new_user1, None)
    except AdminPermissionRequired:
        assert True
        assert AdminPermissionRequired.code == 401
