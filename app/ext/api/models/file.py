from datetime import datetime
from uuid import uuid4

from app.ext.database import db


class Files(db.Model):
    __tablename__ = "files"

    id = db.Column("id", db.String(), primary_key=True, autoincrement=False)
    name = db.Column("name", db.String(100))
    path = db.Column("path", db.String(100))
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())
    updated_at = db.Column("updated_at", db.DateTime, default=datetime.now())

    def __init__(self):
        self.id = str(uuid4())

    def as_dict(self):
        return {"id": self.id, "name": self.name, "path": self.path}
