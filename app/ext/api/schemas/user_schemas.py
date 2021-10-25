from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    name: str
    email: str
    password: str
    admin: bool = False


class UpdateUserSchema(BaseModel):
    name: str = None
    password: str = None
    name: str = None
    admin: bool = None
    email: str = None
