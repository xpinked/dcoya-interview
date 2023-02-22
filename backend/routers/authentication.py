from fastapi import APIRouter, status


from models.token import Token
from models.auth import AuthDetails
from models.user import User, UserData

from utils.security.auth import Auth
from utils.security.hash import Hash

router = APIRouter()


async def get_validated_user(
    authentication_details: AuthDetails,
) -> UserData | None:

    user = await User.find_one(
        User.user_name == authentication_details.user_name,
    )

    if not user or not user.id:
        return None

    is_verified_password = Hash.verify_password(
        plain_password=authentication_details.password,
        hashed_password=user.password
    )

    if not is_verified_password:
        return None

    return UserData(
        id=str(user.id),
        name=user.name,
        user_name=user.user_name,
        role=user.role
    )


@ router.post(
    path='/',
    response_description='Login for access token',
    response_model_exclude_none=True,
    response_model=Token,
    status_code=status.HTTP_201_CREATED,
)
async def login(
    auth_details: AuthDetails,
) -> Token:

    valid_user = await get_validated_user(auth_details)

    if valid_user is None:
        raise Auth.credentials_exception

    access_token = await Auth.create_access_token(
        data=valid_user,
    )

    return Token(
        access_token=access_token,
    )
