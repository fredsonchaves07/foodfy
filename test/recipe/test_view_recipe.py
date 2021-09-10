import json
from io import BytesIO

from app.ext.api.exceptions import InvalidToken, RecipeNotFound
from app.ext.api.services import token_services


def test_view_recipe(client, admin_user):
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

    new_recipe = {
        "name": "recipe test",
        "ingredients": ["Ovo", "Carne de Hamburguer"],
        "preparation_mode": ["Bata um ovo na frigideira", "Frite a carne"],
        "additional_information": "",
        "chef_id": chef.json["id"],
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

    recipe_id = recipe.json.get("id")

    response = client.get(f"/api/v1/recipe/{recipe_id}", headers=headers)

    assert response.content_type == "application/json"
    assert response.status_code == 200
    assert response.json["name"] == new_recipe.get("name")
    assert response.json["ingredients"] == new_recipe.get("ingredients")
    assert response.json["preparation_mode"] == new_recipe.get("preparation_mode")
    assert response.json["chef"].get("name") == new_chef.get("name")
    assert response.json["additional_information"] == new_recipe.get(
        "additional_information"
    )
    assert len(response.json["recipe_imgs"]) == len(new_recipe.get("recipe_imgs"))


def test_no_view_recipe_if_user_is_not_authenticated(admin_user, client):
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

    new_recipe = {
        "name": "recipe test",
        "ingredients": ["Ovo", "Carne de Hamburguer"],
        "preparation_mode": ["Bata um ovo na frigideira", "Frite a carne"],
        "additional_information": "",
        "chef_id": chef.json["id"],
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

    recipe_id = recipe.json.get("id")

    response = client.get(f"/api/v1/recipe/{recipe_id}")

    assert response.content_type == "application/json"
    assert response.status_code == InvalidToken.code
    assert response.json["message"] == InvalidToken.message


def test_no_view_recipe_if_recipe_is_not_already_exist(admin_user, client):
    headers = {
        "Authorization": admin_user.get("token"),
        "content-type": "application/json",
    }

    response = client.get("/api/v1/recipe/105400", headers=headers)

    assert response.content_type == "application/json"
    assert response.status_code == RecipeNotFound.code
    assert response.json["message"] == RecipeNotFound.message
