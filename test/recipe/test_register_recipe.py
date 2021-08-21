import json
from io import BytesIO

from app.ext.api.services import token_services


def test_register_recipe(client, admin_user):
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

    recipe = {
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

    response = client.post(
        "/api/v1/recipe",
        data=recipe,
        headers=headers,
        follow_redirects=True,
        content_type="multipart/form-data",
    )

    assert response.content_type == "application/json"
    assert response.json["name"] == recipe.get("name")
    assert response.json["ingredients"] == recipe.get("ingredients")
    assert response.json["preparation_mode"] == recipe.get("preparation_mode")
    assert response.json["additional_information"] == recipe.get(
        "additional_information"
    )
    assert len(response.json["recipe_imgs"]) == len(recipe.get("recipe_imgs"))

    assert response.status_code == 201
