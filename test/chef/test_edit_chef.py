from io import BytesIO

from app.ext.api.exceptions import AdminPermissionRequired
from app.ext.api.services import token_services


def test_edit_chef(client, admin_user):
    new_chef = {"name": "chef test", "avatar": (BytesIO(b"avatar"), "test.jpg")}

    headers = {"Authorization": admin_user.get("token")}

    chef = client.post(
        "/api/v1/chef",
        data=new_chef,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    chef_id = chef.json.get("id")
    update_chef = {"name": "chef test1"}

    response = client.patch(
        f"/api/v1/chef/{chef_id}", data=update_chef, headers=headers
    )

    assert response.content_type == "application/json"
    assert response.status_code == 200
    assert response.json.get("id") == chef_id
    assert response.json.get("name") == update_chef.get("name")


def test_no_edit_chef_if_user_is_not_admin(client, admin_user):
    new_chef = {"name": "chef test", "avatar": (BytesIO(b"avatar"), "test.jpg")}

    headers = {"Authorization": admin_user.get("token")}

    chef = client.post(
        "/api/v1/chef",
        data=new_chef,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    chef_id = chef.json.get("id")
    update_chef = {"name": "chef test1"}

    token = token_services.generate_token("10", "false_admin@email.com")

    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    try:
        client.patch(f"/api/v1/chef/{chef_id}", data=update_chef, headers=headers)

    except AdminPermissionRequired:
        return True
