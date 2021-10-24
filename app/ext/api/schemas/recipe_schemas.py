from typing import List

from pydantic import BaseModel


class CreateRecipeSchema(BaseModel):
    name: str
    ingredients: List[str]
    preparation_mode: List[str]
    chef_id: str
    additional_information: str = None
    recipe_imgs: List
