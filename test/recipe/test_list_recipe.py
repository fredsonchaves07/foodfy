import json
from io import BytesIO

from app.ext.api.exceptions import InvalidToken
from app.ext.api.services import token_services


def test_list_recipe(client, admin_user):
    new_user1 = {
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
        data=json.dumps(new_user1),
        headers=headers,
    )

    new_chef = {"name": "chef test", "avatar": (BytesIO(b"avatar"), "test.jpg")}

    chef = client.post(
        "/api/v1/chef",
        data=new_chef,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    token = token_services.generate_token(user.json["id"], user.json["email"])
    headers["Authorization"] = token

    recipes = [
        {
            "name": "recipe test 1",
            "ingredients": ["Ovo", "Carne de Hamburguer"],
            "preparation_mode": ["Bata um ovo na frigideira", "Frite a carne"],
            "additional_information": "",
            "chef_id": chef.json["id"],
            "recipe_imgs": [
                (BytesIO(b"recipe_imgs"), "test1.jpg"),
                (BytesIO(b"recipe_imgs"), "test2.jpg"),
            ],
        },
        {
            "name": "recipe test 2",
            "ingredients": ["Ovo", "Carne de Hamburguer"],
            "preparation_mode": ["Bata um ovo na frigideira", "Frite a carne"],
            "additional_information": "",
            "chef_id": chef.json["id"],
            "recipe_imgs": [
                (BytesIO(b"recipe_imgs"), "test1.jpg"),
                (BytesIO(b"recipe_imgs"), "test2.jpg"),
            ],
        },
        {
            "name": "recipe test 3",
            "ingredients": ["Ovo", "Carne de Hamburguer"],
            "preparation_mode": ["Bata um ovo na frigideira", "Frite a carne"],
            "additional_information": "",
            "chef_id": chef.json["id"],
            "recipe_imgs": [
                (BytesIO(b"recipe_imgs"), "test1.jpg"),
                (BytesIO(b"recipe_imgs"), "test2.jpg"),
            ],
        },
    ]

    for recipe in recipes:
        client.post(
            "/api/v1/recipe",
            data=recipe,
            headers=headers,
            follow_redirects=True,
            content_type="multipart/form-data",
        )

    response = client.get("/api/v1/recipe", headers=headers)

    assert response.content_type == "application/json"
    assert response.status_code == 200
    assert len(response.json["recipes"]) == len(recipes)


def test_no_list_recipes_if_user_is_not_authenticate(admin_user, client):
    new_user1 = {
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
        data=json.dumps(new_user1),
        headers=headers,
    )

    new_chef = {"name": "chef test", "avatar": (BytesIO(b"avatar"), "test.jpg")}

    chef = client.post(
        "/api/v1/chef",
        data=new_chef,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    token = token_services.generate_token(user.json["id"], user.json["email"])
    headers["Authorization"] = token

    recipes = [
        {
            "name": "recipe test 1",
            "ingredients": ["Ovo", "Carne de Hamburguer"],
            "preparation_mode": ["Bata um ovo na frigideira", "Frite a carne"],
            "additional_information": "",
            "chef_id": chef.json["id"],
            "recipe_imgs": [
                (BytesIO(b"recipe_imgs"), "test1.jpg"),
                (BytesIO(b"recipe_imgs"), "test2.jpg"),
            ],
        },
        {
            "name": "recipe test 2",
            "ingredients": ["Ovo", "Carne de Hamburguer"],
            "preparation_mode": ["Bata um ovo na frigideira", "Frite a carne"],
            "additional_information": "",
            "chef_id": chef.json["id"],
            "recipe_imgs": [
                (BytesIO(b"recipe_imgs"), "test1.jpg"),
                (BytesIO(b"recipe_imgs"), "test2.jpg"),
            ],
        },
        {
            "name": "recipe test 3",
            "ingredients": ["Ovo", "Carne de Hamburguer"],
            "preparation_mode": ["Bata um ovo na frigideira", "Frite a carne"],
            "additional_information": "",
            "chef_id": chef.json["id"],
            "recipe_imgs": [
                (BytesIO(b"recipe_imgs"), "test1.jpg"),
                (BytesIO(b"recipe_imgs"), "test2.jpg"),
            ],
        },
    ]

    for recipe in recipes:
        client.post(
            "/api/v1/recipe",
            data=recipe,
            headers=headers,
            follow_redirects=True,
            content_type="multipart/form-data",
        )

    response = client.get("/api/v1/recipe")

    assert response.content_type == "application/json"
    assert response.status_code == InvalidToken.code
    assert response.json["message"] == InvalidToken.message
