from app.ext.api.models.user import User
from app.ext.database import db
from werkzeug.security import generate_password_hash


def create_user(name, email, password):
    user = User()
    user.name = name
    user.email = email
    user.password = generate_password_hash(password)

    db.session.add(user)
    db.session.commit()

    return {"id": user.id, "name": user.name, "email": user.email}


def find_by_email(email):
    user = User.query.filter_by(email=email).all()

    return user


def find_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()

    return user


def is_confirmed(user_id):
    user = find_by_id(user_id)

    return user.confirmed


def confirm_user(user_id):
    user = find_by_id(user_id)

    user.confirmed = True
    db.session.add(user)
    db.session.commit()


def is_admin(user_id):
    user = find_by_id(user_id)

    if not user.is_admin:
        return False

    return True
