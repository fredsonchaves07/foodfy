from pydantic import BaseModel


class LoginSchema(BaseModel):
    email: str
    password: str


class ResetPasswordSchema(BaseModel):
    token: str
    password: str
