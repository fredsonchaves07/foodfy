import json
from io import BytesIO

from app.ext.api.exceptions import InvalidToken
from app.ext.api.services import token_services


def test_list_chefs(client, admin_user):
    chefs = [
        {"name": "chef 1", "avatar": (BytesIO(b"avatar"), "chef1.jpg")},
        {"name": "chef 2", "avatar": (BytesIO(b"avatar"), "chef2.jpg")},
        {"name": "chef 3", "avatar": (BytesIO(b"avatar"), "chef3.jpg")},
        {"name": "chef 4", "avatar": (BytesIO(b"avatar"), "chef4.jpg")},
    ]

    headers = {
        "Authorization": admin_user.get("token"),
        "content-type": "application/json",
    }

    for chef in chefs:
        client.post(
            "/api/v1/chef",
            data=chef,
            headers=headers,
            follow_redirects=True,
            content_type="multipart/form-data",
        )

    user1 = {
        "name": "Usuário 1",
        "email": "email1@email.com",
        "password": "123456",
        "admin": False,
    }

    user = client.post(
        "/api/v1/user",
        data=json.dumps(user1),
        headers=headers,
    )

    token = token_services.generate_token(user.json["id"], user.json["email"])

    headers["Authorization"] = token

    response = client.get("/api/v1/chef", headers=headers)

    assert response.content_type == "application/json"
    assert response.status_code == 200
    assert len(response.json["chefs"]) == len(chefs)


def test_no_list_chef_is_user_is_not_authenticate(client, admin_user):
    chefs = [
        {"name": "chef 1", "avatar": (BytesIO(b"avatar"), "chef1.jpg")},
        {"name": "chef 2", "avatar": (BytesIO(b"avatar"), "chef2.jpg")},
        {"name": "chef 3", "avatar": (BytesIO(b"avatar"), "chef3.jpg")},
        {"name": "chef 4", "avatar": (BytesIO(b"avatar"), "chef4.jpg")},
    ]

    headers = {
        "Authorization": admin_user.get("token"),
        "content-type": "application/json",
    }

    for chef in chefs:
        client.post(
            "/api/v1/chef",
            data=chef,
            headers=headers,
            follow_redirects=True,
            content_type="multipart/form-data",
        )

    headers["Authorization"] = None

    response = client.get("/api/v1/chef", headers=headers)

    assert response.status_code == InvalidToken.code
    assert response.json["message"] == InvalidToken.message
