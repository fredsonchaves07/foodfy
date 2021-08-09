from app.ext.api.models.chef import Chef
from app.ext.database import db


def create_chef(name, avatar):
    chef = Chef()

    chef.name = name
    chef.file_id = avatar

    db.session.add(chef)
    db.session.commit()

    return chef.as_dict()
