import json
from io import BytesIO

from app.ext.api.exceptions import ChefNotFound
from app.ext.api.services import token_services


def test_view_chef(client, admin_user):
    new_chef = {"name": "chef test", "avatar": (BytesIO(b"avatar"), "test.jpg")}
    new_user = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    headers = {
        "Authorization": admin_user.get("token"),
        "content-type": "application/json",
    }

    chef = client.post(
        "/api/v1/chef",
        data=new_chef,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    user = client.post(
        "/api/v1/user",
        data=json.dumps(new_user),
        headers=headers,
    )

    chef_id = chef.json.get("id")
    chef_name = chef.json.get("name")
    avatar = chef.json.get("avatar")
    user_id = user.json.get("id")
    email = user.json.get("email")

    token = token_services.generate_token(user_id, email)

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    response = client.get(f"/api/v1/chef/{chef_id}", headers=headers)

    assert response.content_type == "application/json"
    assert response.status_code == 200
    assert response.json.get("id") == chef_id
    assert response.json.get("name") == chef_name
    assert response.json.get("avatar") == avatar


def test_no_view_chef_if_chef_not_already_exist(client, admin_user):
    new_user = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    headers = {
        "Authorization": admin_user.get("token"),
        "content-type": "application/json",
    }

    user = client.post(
        "/api/v1/user",
        data=json.dumps(new_user),
        headers=headers,
    )

    user_id = user.json.get("id")
    email = user.json.get("email")

    token = token_services.generate_token(user_id, email)

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    response = client.get("/api/v1/chef/1010", headers=headers)

    assert response.status_code == ChefNotFound.code
    assert response.json["message"] == ChefNotFound.message
