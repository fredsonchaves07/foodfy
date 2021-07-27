import json

from app.ext.api.services import token_services


def test_create_user(client, database):
    token = token_services.generate_token("1", "admin@email.com")

    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    headers = {"Authorization": token, "content-type": "application/json"}

    response = client.post(
        "/api/v1/user",
        data=json.dumps(new_user1),
        headers=headers,
    )

    assert response.content_type == "application/json"
    assert response.json["email"] == new_user1["email"]


# def test_no_create_user_if_email_already_exist(app, database):
#     new_user1 = {
#         "name": "Usuário teste",
#         "email": "email@email.com",
#         "password": "12346",
#     }

#     users_controller.create_user(new_user1, "admin@email.com")

#     new_user2 = {
#         "name": "Usuário teste2",
#         "email": "email@email.com",
#         "password": "12564",
#     }

#     try:
#         users_controller.create_user(new_user2, "admin@email.com")
#     except EmailAlreadyExist:
#         assert True
#         assert EmailAlreadyExist.code == 422


# def test_no_create_user_if_not_admin(app, database):
#     new_user1 = {
#         "name": "Usuário teste",
#         "email": "email@email.com",
#         "password": "12346",
#     }

#     try:
#         users_controller.create_user(new_user1, None)
#     except AdminPermissionRequired:
#         assert True
#         assert AdminPermissionRequired.code == 401


# def test_confirm_user(app, database):
#     new_user1 = {
#         "name": "Usuário teste",
#         "email": "email@email.com",
#         "password": "12346",
#     }

#     user = users_controller.create_user(new_user1, "admin@email.com")

#     users_controller.confirm_user(user["id"])

#     assert True


# def test_no_user_confirmed(app, database):
#     new_user1 = {
#         "name": "Usuário teste",
#         "email": "email@email.com",
#         "password": "12346",
#     }

#     user = users_controller.create_user(new_user1, "admin@email.com")

#     users_controller.confirm_user(user["id"])
#     assert users_controller.confirm_user(user["id"]) is False
