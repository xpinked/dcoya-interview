from datetime import datetime
from pydantic import BaseModel

from models.user import UserData


class Token(BaseModel):
    access_token: str
    token_type: str = 'Bearer'


class TokenData(BaseModel):
    exp: datetime
    iat: datetime
    sub: str
    data: UserData


class EncodedToken(TokenData):
    pass


class DecodedToken(TokenData):
    pass
