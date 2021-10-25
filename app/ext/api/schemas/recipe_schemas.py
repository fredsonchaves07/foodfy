from typing import List

from pydantic import BaseModel


class CreateRecipeSchema(BaseModel):
    name: str
    ingredients: List[str]
    preparation_mode: List[str]
    chef_id: str
    additional_information: str = None
    recipe_imgs: List


class UpdateRecipeSchema(BaseModel):
    name: str = None
    ingredients: List[str] = None
    preparation_mode: List[str] = None
    chef_id: str = None
    additional_information: str = None
    recipe_imgs: List = None
    delete_imgs: List[str] = None
