from app.ext.api.exceptions import FileNotFound
from app.ext.api.services import file_services
from app.ext.api.utils import file_utils


def create_file(file):
    if not file:
        raise FileNotFound

    file_uploaded = file_utils.upload(file)

    new_file = file_services.create_file(
        file_uploaded.get("filename"), file_uploaded.get("path")
    )

    return new_file


def update_file(file_id, file):
    if not file:
        return {}

    file_old = file_services.get_file_by_id(file_id)

    file_utils.remove(file_old)
    file_uploaded = file_utils.upload(file)

    update_file = file_services.update_file(
        file_id, file_uploaded.get("filename"), file_uploaded.get("path")
    )

    return update_file


def delete_file(file_id):
    file_old = file_services.get_file_by_id(file_id)

    if not file_old:
        raise FileNotFound

    file_services.delete_file(file_id)
    file_utils.remove(file_old)
