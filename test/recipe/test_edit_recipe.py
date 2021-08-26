import json
from io import BytesIO

from app.ext.api.services import token_services


def test_edit_recipe(client, admin_user):
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

    recipe_id = recipe.json["id"]
    old_imgs = [recipe_img.get("file_id") for recipe_img in recipe.json["recipe_imgs"]]

    update_recipe = {
        "name": "recipe updated",
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
    assert len(response.json.get("recipe_imgs")) == len(
        update_recipe.get("recipe_imgs")
    )
