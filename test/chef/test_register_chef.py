from io import BytesIO

from app.ext.api.exceptions import AdminPermissionRequired, FileNotFound
from app.ext.api.services import token_services


def test_register_chef(client, admin_user):
    new_chef = {"name": "chef test", "avatar": (BytesIO(b"avatar"), "test.jpg")}

    headers = {"Authorization": admin_user.get("token")}

    response = client.post(
        "/api/v1/chef",
        data=new_chef,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    assert response.content_type == "application/json"
    assert response.status_code == 201
    assert response.json["name"] == new_chef.get("name")


def test_no_register_chef_if_file_not_found(client, admin_user):
    new_chef = {"name": "chef test"}

    headers = {"Authorization": admin_user.get("token")}

    try:
        client.post(
            "/api/v1/chef",
            data=new_chef,
            headers=headers,
            follow_redirects=True,
            content_type="multipart/form-data",
        )
    except FileNotFound:
        return True


def test_no_register_chef_if_user_not_admin(client, database):
    token = token_services.generate_token("10", "false_admin@email.com")

    new_chef = {"name": "chef test", "avatar": (BytesIO(b"avatar"), "test.jpg")}

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    try:
        client.post(
            "/api/v1/chef",
            data=new_chef,
            headers=headers,
            follow_redirects=True,
            content_type="multipart/form-data",
        )
    except AdminPermissionRequired:
        return True
