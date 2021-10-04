from app.ext.api.controller import file_controller
from app.ext.api.exceptions import ChefNotFound, RecipeLinkedChef
from app.ext.api.services import chef_services
from flask import session


def create_chef(chef, file):
    name = chef.get("name")

    new_file = file_controller.create_file(file)

    chef = chef_services.create_chef(name, new_file.get("id"))

    session["audit_log"] = {
        "object_type": "CHEF",
        "object_id": chef.get("id"),
        "object_name": chef.get("name"),
        "action": "CREATE",
    }

    return chef


def update_chef(chef_id, chef_data, file):
    chef = chef_services.find_by_id(chef_id)

    if not chef:
        raise ChefNotFound

    name = chef_data.get("name")

    file_controller.update_file(chef.file_id, file)

    chef = chef_services.update_chef(chef_id, name)

    session["audit_log"] = {
        "object_type": "CHEF",
        "object_id": chef.get("id"),
        "object_name": chef.get("name"),
        "action": "UPDATE",
    }

    return chef


def delete_chef(chef_id):
    chef = chef_services.find_by_id(chef_id)

    if not chef:
        raise ChefNotFound

    if chef_services.is_recipe_linked_chef(chef_id):
        raise RecipeLinkedChef

    chef_services.delete_chef(chef_id)

    session["audit_log"] = {
        "object_type": "CHEF",
        "object_id": chef.id,
        "object_name": chef.name,
        "action": "DELETE",
    }


def get_chef(chef_id):
    chef = chef_services.find_by_id(chef_id)

    if not chef:
        raise ChefNotFound

    return chef.as_dict()


def list_chef():
    chefs = chef_services.list_chef()

    return {"chefs": chefs}
