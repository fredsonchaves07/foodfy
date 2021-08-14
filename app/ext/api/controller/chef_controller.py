from app.ext.api.controller import file_controller
from app.ext.api.exceptions import ChefNotFound
from app.ext.api.services import chef_services


def create_chef(chef, file):
    name = chef.get("name")

    new_file = file_controller.create_file(file)

    chef = chef_services.create_chef(name, new_file.get("id"))

    return chef


def update_chef(chef_id, chef_data, file):
    chef = chef_services.find_by_id(chef_id)

    if not chef:
        raise ChefNotFound

    name = chef_data.get("name")

    file_controller.update_file(chef.file_id, file)

    chef = chef_services.update_chef(chef_id, name)

    return chef


def delete_chef(chef_id):
    chef = chef_services.find_by_id(chef_id)

    if not chef:
        raise ChefNotFound

    chef_services.delete_chef(chef_id)
