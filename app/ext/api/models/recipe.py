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
    user_id = db.Column("user_id", db.String, db.ForeignKey("user.id"))
    chef_id = db.Column("chef_id", db.String, db.ForeignKey("chef.id"))
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())
    updated_at = db.Column("updated_at", db.DateTime, default=datetime.now())
    chef = db.relationship(
        "Chef", lazy="select", backref=db.backref("recipe", lazy="joined")
    )
    recipe_files = db.relationship(
        "RecipeFiles", lazy="select", backref=db.backref("recipe", lazy="joined")
    )

    def __init__(self):
        self.id = str(uuid4())

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "chef": self.chef.as_dict(),
            "preparation_mode": self.preparation_mode,
            "ingredients": self.ingredients,
            "additional_information": self.additional_information,
        }
