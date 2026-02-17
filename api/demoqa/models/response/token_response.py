from pydantic import BaseModel


class TokenResponse(BaseModel):
    token: str
    expires: str
    status: str
    result: str
