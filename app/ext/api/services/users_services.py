from app.ext.api.models.user import User
from app.ext.database import db
from werkzeug.security import check_password_hash, generate_password_hash


def create_user(name, email, password, admin=False):
    user = User()

    user.name = name
    user.email = email
    user.is_admin = admin
    user.password = generate_password_hash(password)

    db.session.add(user)
    db.session.commit()

    return user.as_dict()


def find_by_email(email):
    user = User.query.filter_by(email=email).first()

    return user


def find_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()

    return user


def is_confirmed(user_id):
    user = find_by_id(user_id)

    if not user:
        return False

    return user.confirmed


def confirm_user(user_id):
    user = find_by_id(user_id)

    if not user:
        return False

    user.confirmed = True
    db.session.add(user)
    db.session.commit()

    return user.as_dict()


def is_admin(user_id):
    user = find_by_id(user_id)

    if not user:
        return False

    return user.is_admin


def password_reset(user_id, password):
    user = find_by_id(user_id)

    user.password = generate_password_hash(password)

    db.session.add(user)
    db.session.commit()

    return user.as_dict()


def password_match(email, password):
    user = find_by_email(email)

    return check_password_hash(user.password, password)


def list_user():
    users = User.query.all()

    return [user.as_dict() for user in users]


def update_user(user_id, email, password, name):
    user = find_by_id(user_id)

    if email:
        user.email = email

    if password:
        user.password = generate_password_hash(password)

    if name:
        user.name = name

    db.session.commit()

    return user


def delete_user(user_id):
    user = find_by_id(user_id)

    db.session.delete(user)
