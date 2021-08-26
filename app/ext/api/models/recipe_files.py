from datetime import datetime
from uuid import uuid4

from app.ext.database import db


class RecipeFiles(db.Model):
    __tablename__ = "recipe_files"

    id = db.Column("id", db.String, primary_key=True, autoincrement=False)
    recipe_id = db.Column(
        "recipe_id", db.String, db.ForeignKey("recipe.id"), nullable=False
    )
    file_id = db.Column("file_id", db.String, db.ForeignKey("files.id"), nullable=False)
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())
    updated_at = db.Column("updated_at", db.DateTime, default=datetime.now())
    files = db.relationship(
        "Files", lazy="select", backref=db.backref("recipe_files", lazy="joined")
    )

    def __init__(self):
        self.id = str(uuid4())

    def as_dict(self):
        return {
            "recipe_id": self.recipe_id,
            "path": self.files.path,
            "file_id": self.file_id,
        }
