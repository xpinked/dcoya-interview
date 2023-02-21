from datetime import datetime
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str = 'Bearer'


class TokenData(BaseModel):
    id: str


class EncodedToken(BaseModel):
    exp: datetime
    iat: datetime
    sub: str
