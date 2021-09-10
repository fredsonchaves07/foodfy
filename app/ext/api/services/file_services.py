from app.ext.api.models.file import Files
from app.ext.database import db


def create_file(filename, path):
    file = Files()

    file.name = filename
    file.path = path

    db.session.add(file)
    db.session.commit()

    return file.as_dict()


def update_file(file_id, filename, path):
    file = get_file_by_id(file_id)

    file.name = filename
    file.path = path

    db.session.commit()

    return file.as_dict()


def get_file_by_id(file_id):
    file = Files.query.filter_by(id=file_id).first()

    return file


def delete_file(file_id):
    file = get_file_by_id(file_id)

    db.session.delete(file)
    db.session.commit()
