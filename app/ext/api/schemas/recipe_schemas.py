from typing import List

from pydantic import BaseModel
from werkzeug.datastructures import FileStorage


class CreateRecipeSchema(BaseModel):
    name: str
    ingredients: List[str]
    preparation_mode: List[str]
    chef_id: str
    additional_information: str = None
    recipe_imgs: List[FileStorage]

    class Config:
        arbitrary_types_allowed = True


class UpdateRecipeSchema(BaseModel):
    name: str = None
    ingredients: List[str] = None
    preparation_mode: List[str] = None
    chef_id: str = None
    additional_information: str = None
    recipe_imgs: List[FileStorage] = None
    delete_imgs: List[str] = None

    class Config:
        arbitrary_types_allowed = True
