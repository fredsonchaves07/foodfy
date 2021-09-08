from io import BytesIO

from app.ext.api.exceptions import (
    AdminPermissionRequired,
    ChefNotFound,
    RecipeLinkedChef,
)
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


def test_no_edit_chef_if_chef_is_not_already_exist(client, admin_user, database):
    headers = {"Authorization": admin_user.get("token")}

    update_chef = {"name": "chef test1"}

    response = client.patch("/api/v1/chef/1000000", data=update_chef, headers=headers)

    assert response.status_code == ChefNotFound.code
    assert response.json["message"] == ChefNotFound.message


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

    response = client.patch(
        f"/api/v1/chef/{chef_id}", data=update_chef, headers=headers
    )

    assert response.status_code == AdminPermissionRequired.code
    assert response.json["message"] == AdminPermissionRequired.message


def test_delete_chef(client, admin_user):
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

    response = client.delete(f"/api/v1/chef/{chef_id}", headers=headers)

    assert response.content_type == "application/json"
    assert response.status_code == 204


def test_no_delete_if_chef_is_not_already_exist(client, admin_user):
    headers = {"Authorization": admin_user.get("token")}

    response = client.delete("/api/v1/chef/10", headers=headers)

    assert response.status_code == ChefNotFound.code
    assert response.json["message"] == ChefNotFound.message


def test_no_delete_if_recipe_linked_chef(client, admin_user):
    new_chef = {"name": "chef test", "avatar": (BytesIO(b"avatar"), "test.jpg")}

    headers = {"Authorization": admin_user.get("token")}

    chef = client.post(
        "/api/v1/chef",
        data=new_chef,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    chef_id = chef.json["id"]

    recipe = {
        "name": "recipe test",
        "ingredients": ["Ovo", "Carne de Hamburguer"],
        "preparation_mode": ["Bata um ovo na frigideira", "Frite a carne"],
        "additional_information": "",
        "chef_id": chef_id,
        "recipe_imgs": [
            (BytesIO(b"recipe_imgs"), "test1.jpg"),
            (BytesIO(b"recipe_imgs"), "test2.jpg"),
        ],
    }

    client.post(
        "/api/v1/recipe",
        data=recipe,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    response = client.delete(f"/api/v1/chef/{chef_id}", headers=headers)

    assert response.status_code == RecipeLinkedChef.code
    assert response.json["message"] == RecipeLinkedChef.message


def test_update_avatar_file_chef(client, admin_user):
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
    avatar = chef.json.get("avatar")

    update_chef = {"avatar": (BytesIO(b"avatar1"), "test.jpg")}

    response = client.patch(
        f"/api/v1/chef/{chef_id}", data=update_chef, headers=headers
    )

    assert response.content_type == "application/json"
    assert response.status_code == 200
    assert response.json.get("id") == chef_id
    assert response.json.get("avatar") != avatar
