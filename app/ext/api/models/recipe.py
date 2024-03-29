import json
from datetime import datetime
from uuid import uuid4

from app.ext.database import db


class Recipe(db.Model):
    __tablename__ = "recipe"

    id = db.Column("id", db.String, primary_key=True, autoincrement=False)
    name = db.Column("name", db.String(100), nullable=False)
    ingredients = db.Column("ingredients", db.JSON)
    preparation_mode = db.Column("preparation", db.JSON)
    additional_information = db.Column("additional_information", db.String)
    user_id = db.Column("user_id", db.String, db.ForeignKey("user.id"), nullable=False)
    chef_id = db.Column("chef_id", db.String, db.ForeignKey("chef.id"), nullable=False)
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())
    updated_at = db.Column("updated_at", db.DateTime, default=datetime.now())
    chef = db.relationship(
        "Chef", lazy="select", backref=db.backref("recipe", lazy="joined")
    )
    recipe_files = db.relationship(
        "RecipeFiles",
        lazy="select",
        cascade="all, delete-orphan",
        backref=db.backref("recipe", lazy="joined"),
    )

    def __init__(self):
        self.id = str(uuid4())

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "chef": self.chef.as_dict(),
            "preparation_mode": json.loads(self.preparation_mode),
            "ingredients": json.loads(self.ingredients),
            "additional_information": self.additional_information,
            "recipe_imgs": [recipe_img.as_dict() for recipe_img in self.recipe_files],
        }
