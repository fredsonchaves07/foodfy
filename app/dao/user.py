from app.db import db
from app.db.models import User


def login(email, password):
    user = Chef.query.filter(email=email, password=password).first()
    
    return user
