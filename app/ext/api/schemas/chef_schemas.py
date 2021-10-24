from pydantic import BaseModel
from werkzeug.datastructures import FileStorage


class CreateChefSchema(BaseModel):
    name: str
    avatar: FileStorage = None

    class Config:
        arbitrary_types_allowed = True


class UpdateChefSchema(BaseModel):
    name: str = None
    avatar: FileStorage = None

    class Config:
        arbitrary_types_allowed = True
