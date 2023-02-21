from beanie import PydanticObjectId
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

from configurations.config import settings
from models.user import User
from models.token import TokenData, EncodedToken


class AuthBearer(HTTPBearer):
    pass


class Auth:
    auth_scheme = AuthBearer()

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    @classmethod
    async def encode_token(
        cls,
        data: TokenData,
    ) -> str:

        encoded_token = EncodedToken(
            exp=datetime.utcnow() + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            ),
            iat=datetime.utcnow(),
            sub=data.id,
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
    ) -> TokenData:

        try:
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=settings.JWT_ALGORITHM,
            )

            sub = str(payload.get('sub'))

            if sub is None:
                raise cls.credentials_exception

            return TokenData(id=sub)

        except JWTError:
            raise cls.credentials_exception

    @classmethod
    async def get_current_user(
        cls,
        auth: HTTPAuthorizationCredentials = Security(auth_scheme),
    ) -> User:

        token_data = await cls.decode_token(auth.credentials)

        user = await User.get(
            document_id=PydanticObjectId(token_data.id),
        )

        if user is None:
            raise cls.credentials_exception

        return user

    @classmethod
    async def create_access_token(
        cls,
        data: TokenData,
        expires_delta: timedelta | None = None
    ) -> str:

        encoded_jwt = await cls.encode_token(data=data)

        return encoded_jwt
