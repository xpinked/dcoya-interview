from beanie import PydanticObjectId
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt, ExpiredSignatureError

from configurations.config import settings
from models.user import UserData
from models.token import EncodedToken, DecodedToken


class AuthBearer(HTTPBearer):
    pass


class Auth:
    auth_scheme = AuthBearer()

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    expired_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Your token is expired please authenticate again",
        headers={"WWW-Authenticate": "Bearer"},
    )

    @classmethod
    async def encode_token(
        cls,
        data: UserData,
    ) -> str:

        encoded_token = EncodedToken(
            exp=datetime.utcnow() + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            ),
            iat=datetime.utcnow(),
            sub=str(data.id),
            data=data,
        )

        return jwt.encode(
            encoded_token.dict(),
            settings.SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM,
        )

    @classmethod
    async def decode_token(
        cls,
        token: str,
    ) -> DecodedToken:

        try:
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=settings.JWT_ALGORITHM,
            )

            decoded_token = DecodedToken(**payload)

            return decoded_token

        except ExpiredSignatureError:
            raise cls.expired_exception

        except JWTError:
            raise cls.credentials_exception

    @classmethod
    async def get_current_user(
        cls,
        auth: HTTPAuthorizationCredentials = Security(auth_scheme),
    ) -> UserData:

        token_data = await cls.decode_token(auth.credentials)

        return token_data.data

    @classmethod
    async def create_access_token(
        cls,
        data: UserData,
    ) -> str:

        encoded_jwt = await cls.encode_token(data=data)

        return encoded_jwt
