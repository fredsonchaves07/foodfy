from app.ext.api.models.user import User
from app.ext.database import db


def create_user(name, email, password):
    user = User()
    user.name = name
    user.email = email
    user.password = password

    db.session.add(user)
    db.session.commit()

    return {"id": user.id, "name": user.name, "email": user.email}


def find_by_email(email):
    user = User.query.filter_by(email=email).all()

    return user
