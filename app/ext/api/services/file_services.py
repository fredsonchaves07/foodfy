from app.ext.api.models.file import Files
from app.ext.database import db


def create_file(filename, path):
    file = Files()

    file.name = filename
    file.path = path

    db.session.add(file)
    db.session.commit()

    return file.as_dict()
