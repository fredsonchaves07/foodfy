from app.ext.api.services import chef_services, file_services
from app.ext.api.utils import file_utils


def create_chef(chef, file):
    name = chef.get("name")

    file_uploaded = file_utils.upload(file)

    avatar_chef = file_services.create_file(
        file_uploaded.get("filename"), file_uploaded.get("path")
    )

    chef = chef_services.create_chef(name, avatar_chef.get("id"))

    return chef
