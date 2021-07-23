from datetime import datetime
from uuid import uuid4

from app.ext.database import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column("id", db.String(), primary_key=True, autoincrement=False)
    name = db.Column("name", db.String(100), nullable=False)
    email = db.Column("email", db.String(100), nullable=False, unique=True)
    password = db.Column("password", db.String(), nullable=False)
    is_admin = db.Column("is_admin", db.Boolean(), default=False)
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())
    updated_at = db.Column("updated_at", db.DateTime, default=datetime.now())

    def __init__(self):
        self.id = str(uuid4())
