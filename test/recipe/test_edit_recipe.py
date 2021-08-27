import json
from io import BytesIO

from app.ext.api.exceptions import InvalidToken, InvalidUser, MaximumImageCapacityError
from app.ext.api.services import token_services


def test_edit_recipe(client, admin_user):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    new_chef1 = {"name": "chef test", "avatar": (BytesIO(b"avatar"), "test.jpg")}
    new_chef2 = {"name": "chef test", "avatar": (BytesIO(b"avatar"), "test.jpg")}

    headers = {
        "Authorization": admin_user.get("token"),
        "content-type": "application/json",
    }

    user1 = client.post(
        "/api/v1/user",
        data=json.dumps(new_user1),
        headers=headers,
    )

    chef1 = client.post(
        "/api/v1/chef",
        data=new_chef1,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    chef2 = client.post(
        "/api/v1/chef",
        data=new_chef2,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    token = token_services.generate_token(user1.json["id"], user1.json["email"])
    headers["Authorization"] = token

    new_recipe = {
        "name": "recipe test",
        "ingredients": ["Ovo", "Carne de Hamburguer"],
        "preparation_mode": ["Bata um ovo na frigideira", "Frite a carne"],
        "additional_information": "",
        "chef_id": chef1.json["id"],
        "recipe_imgs": [
            (BytesIO(b"recipe_imgs"), "test1.jpg"),
            (BytesIO(b"recipe_imgs"), "test2.jpg"),
        ],
    }

    recipe = client.post(
        "/api/v1/recipe",
        data=new_recipe,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    recipe_id = recipe.json["id"]
    old_imgs = [recipe_img.get("file_id") for recipe_img in recipe.json["recipe_imgs"]]

    update_recipe = {
        "name": "recipe updated",
        "chef_id": chef2.json["id"],
        "ingredients": ["Ovo", "Carne de Hamburguer", "Salada"],
        "preparation_mode": ["Bata um ovo na frigideira", "Coloque a salada"],
        "delete_imgs": old_imgs,
        "recipe_imgs": [
            (BytesIO(b"recipe_imgs"), "test-alterado.jpg"),
        ],
    }

    response = client.patch(
        f"/api/v1/recipe/{recipe_id}",
        data=update_recipe,
        headers=headers,
        content_type="multipart/form-data",
    )

    assert response.content_type == "application/json"
    assert response.status_code == 200
    assert response.json.get("id") == recipe_id
    assert response.json.get("name") == update_recipe.get("name")
    assert response.json.get("chef").get("id") == update_recipe.get("chef_id")
    assert len(response.json.get("recipe_imgs")) == len(
        update_recipe.get("recipe_imgs")
    )
    for ingredient in response.json.get("ingredients"):
        assert ingredient in update_recipe.get("ingredients")
    for preparation_mode in response.json.get("preparation_mode"):
        assert preparation_mode in update_recipe.get("preparation_mode")


def test_edit_recipe_other_users_if_user_is_admin(client, admin_user):
    headers = {
        "Authorization": admin_user.get("token"),
        "content-type": "application/json",
    }

    users = [
        {
            "name": "Usuário teste",
            "email": "email@email.com",
            "password": "123456",
            "admin": False,
        },
        {
            "name": "Usuário teste",
            "email": "email1@email.com",
            "password": "123456",
            "admin": False,
        },
    ]

    users_created = []

    for user in users:
        user_info = client.post(
            "/api/v1/user",
            data=json.dumps(user),
            headers=headers,
        )

        users_created.append(user_info)

    new_chef1 = {"name": "chef test", "avatar": (BytesIO(b"avatar"), "test.jpg")}

    chef1 = client.post(
        "/api/v1/chef",
        data=new_chef1,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    ids_recipe_list = []

    for user in users_created:
        token = token_services.generate_token(user.json["id"], user.json["email"])
        headers["Authorization"] = token

        new_recipe = {
            "name": "recipe test",
            "ingredients": ["Ovo", "Carne de Hamburguer"],
            "preparation_mode": ["Bata um ovo na frigideira", "Frite a carne"],
            "additional_information": "",
            "chef_id": chef1.json["id"],
            "recipe_imgs": [
                (BytesIO(b"recipe_imgs"), "test1.jpg"),
                (BytesIO(b"recipe_imgs"), "test2.jpg"),
            ],
        }

        recipe = client.post(
            "/api/v1/recipe",
            data=new_recipe,
            headers=headers,
            follow_redirects=True,
            content_type="multipart/form-data",
        )

        ids_recipe_list.append(recipe.json["id"])

    update_recipe = {
        "name": "recipe updated",
        "chef_id": chef1.json["id"],
        "ingredients": ["Ovo", "Carne de Hamburguer", "Salada"],
        "preparation_mode": ["Bata um ovo na frigideira", "Coloque a salada"],
    }

    headers["Authorization"] = admin_user.get("token")

    response = client.patch(
        f"/api/v1/recipe/{ids_recipe_list[0]}",
        data=update_recipe,
        headers=headers,
        content_type="multipart/form-data",
    )

    assert response.content_type == "application/json"
    assert response.status_code == 200
    assert response.json.get("name") == update_recipe.get("name")
    assert response.json.get("chef").get("id") == update_recipe.get("chef_id")

    for ingredient in response.json.get("ingredients"):
        assert ingredient in update_recipe.get("ingredients")
    for preparation_mode in response.json.get("preparation_mode"):
        assert preparation_mode in update_recipe.get("preparation_mode")


def test_no_edit_recipe_if_user_not_authenticated(client, admin_user):
    headers = {
        "Authorization": admin_user.get("token"),
        "content-type": "application/json",
    }

    new_chef1 = {"name": "chef test", "avatar": (BytesIO(b"avatar"), "test.jpg")}

    chef1 = client.post(
        "/api/v1/chef",
        data=new_chef1,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    new_recipe = {
        "name": "recipe test",
        "ingredients": ["Ovo", "Carne de Hamburguer"],
        "preparation_mode": ["Bata um ovo na frigideira", "Frite a carne"],
        "additional_information": "",
        "chef_id": chef1.json["id"],
        "recipe_imgs": [
            (BytesIO(b"recipe_imgs"), "test1.jpg"),
            (BytesIO(b"recipe_imgs"), "test2.jpg"),
        ],
    }

    recipe = client.post(
        "/api/v1/recipe",
        data=new_recipe,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    recipe_id = recipe.json["id"]

    update_recipe = {
        "name": "recipe updated",
        "ingredients": ["Ovo", "Carne de Hamburguer", "Salada"],
        "preparation_mode": ["Bata um ovo na frigideira", "Coloque a salada"],
        "recipe_imgs": [
            (BytesIO(b"recipe_imgs"), "test-alterado.jpg"),
        ],
    }

    response = client.patch(
        f"/api/v1/recipe/{recipe_id}",
        data=update_recipe,
        content_type="multipart/form-data",
    )

    assert response.status_code == InvalidToken.code
    assert response.json["message"] == InvalidToken.message


def test_no_edit_recipe_if_recipe_is_other_user(client, admin_user):
    headers = {
        "Authorization": admin_user.get("token"),
        "content-type": "application/json",
    }

    users = [
        {
            "name": "Usuário teste",
            "email": "email@email.com",
            "password": "123456",
            "admin": False,
        },
        {
            "name": "Usuário teste",
            "email": "email1@email.com",
            "password": "123456",
            "admin": False,
        },
    ]

    users_created = []

    for user in users:
        user_info = client.post(
            "/api/v1/user",
            data=json.dumps(user),
            headers=headers,
        )

        users_created.append(user_info)

    new_chef1 = {"name": "chef test", "avatar": (BytesIO(b"avatar"), "test.jpg")}

    chef1 = client.post(
        "/api/v1/chef",
        data=new_chef1,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    ids_recipe_list = []

    for user in users_created:
        token = token_services.generate_token(user.json["id"], user.json["email"])
        headers["Authorization"] = token

        new_recipe = {
            "name": "recipe test",
            "ingredients": ["Ovo", "Carne de Hamburguer"],
            "preparation_mode": ["Bata um ovo na frigideira", "Frite a carne"],
            "additional_information": "",
            "chef_id": chef1.json["id"],
            "recipe_imgs": [
                (BytesIO(b"recipe_imgs"), "test1.jpg"),
                (BytesIO(b"recipe_imgs"), "test2.jpg"),
            ],
        }

        recipe = client.post(
            "/api/v1/recipe",
            data=new_recipe,
            headers=headers,
            follow_redirects=True,
            content_type="multipart/form-data",
        )

        ids_recipe_list.append(recipe.json["id"])

    update_recipe = {
        "name": "recipe updated",
        "chef_id": chef1.json["id"],
        "ingredients": ["Ovo", "Carne de Hamburguer", "Salada"],
        "preparation_mode": ["Bata um ovo na frigideira", "Coloque a salada"],
    }

    response = client.patch(
        f"/api/v1/recipe/{ids_recipe_list[0]}",
        data=update_recipe,
        headers=headers,
        content_type="multipart/form-data",
    )

    assert response.status_code == InvalidUser.code
    assert response.json["message"] == InvalidUser.message


def test_no_edit_recipe_if_have_maximum_capacity_images(client, admin_user):
    new_user1 = {
        "name": "Usuário teste",
        "email": "email@email.com",
        "password": "123456",
        "admin": False,
    }

    new_chef1 = {"name": "chef test", "avatar": (BytesIO(b"avatar"), "test.jpg")}

    headers = {
        "Authorization": admin_user.get("token"),
        "content-type": "application/json",
    }

    user1 = client.post(
        "/api/v1/user",
        data=json.dumps(new_user1),
        headers=headers,
    )

    chef1 = client.post(
        "/api/v1/chef",
        data=new_chef1,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    token = token_services.generate_token(user1.json["id"], user1.json["email"])
    headers["Authorization"] = token

    new_recipe = {
        "name": "recipe test",
        "ingredients": ["Ovo", "Carne de Hamburguer"],
        "preparation_mode": ["Bata um ovo na frigideira", "Frite a carne"],
        "additional_information": "",
        "chef_id": chef1.json["id"],
        "recipe_imgs": [
            (BytesIO(b"recipe_imgs"), "test1.jpg"),
        ],
    }

    recipe = client.post(
        "/api/v1/recipe",
        data=new_recipe,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    recipe_id = recipe.json["id"]

    update_recipe = {
        "name": "recipe updated",
        "chef_id": chef1.json["id"],
        "ingredients": ["Ovo", "Carne de Hamburguer", "Salada"],
        "preparation_mode": ["Bata um ovo na frigideira", "Coloque a salada"],
        "recipe_imgs": [
            (BytesIO(b"recipe_imgs"), "test-alterado.jpg"),
            (BytesIO(b"recipe_imgs"), "test-alterado.jpg"),
            (BytesIO(b"recipe_imgs"), "test-alterado.jpg"),
            (BytesIO(b"recipe_imgs"), "test-alterado.jpg"),
            (BytesIO(b"recipe_imgs"), "test-alterado.jpg"),
            (BytesIO(b"recipe_imgs"), "test-alterado.jpg"),
        ],
    }

    response = client.patch(
        f"/api/v1/recipe/{recipe_id}",
        data=update_recipe,
        headers=headers,
        content_type="multipart/form-data",
    )

    assert response.content_type == "application/json"
    assert response.status_code == MaximumImageCapacityError.code
    assert response.json["message"] == MaximumImageCapacityError.message
