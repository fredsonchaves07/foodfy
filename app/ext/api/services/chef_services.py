from app.ext.api.models.chef import Chef
from app.ext.database import db


def create_chef(name, avatar):
    chef = Chef()

    chef.name = name
    chef.file_id = avatar

    db.session.add(chef)
    db.session.commit()

    return chef.as_dict()


def find_by_id(chef_id):
    chef = Chef.query.filter_by(id=chef_id).first()

    return chef


def update_chef(chef_id, name):
    chef = Chef.query.filter_by(id=chef_id).first()

    if name:
        chef.name = name

    db.session.commit()

    return chef.as_dict()


def delete_chef(chef_id):
    chef = find_by_id(chef_id)

    db.session.delete(chef)
    db.session.commit()


def list_chef():
    chefs = Chef.query.all()

    return [chef.as_dict() for chef in chefs]


def is_recipe_linked_chef(chef_id):
    chef = find_by_id(chef_id)

    if chef.recipe:
        return True

    return False
