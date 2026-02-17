from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    userName: str
    password: str
