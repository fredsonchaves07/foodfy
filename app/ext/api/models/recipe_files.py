from datetime import datetime

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
