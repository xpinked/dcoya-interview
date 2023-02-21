from beanie import PydanticObjectId
from fastapi import APIRouter, status
from utils.security.hash import Hash

from models.user import User, ShowUser
from models.response import Response

import exceptions.users_exceptions as users_exceptions

router = APIRouter()


@router.post(
    path='/',
    response_description='Register a User new user',
    response_model_exclude_none=True,
    status_code=status.HTTP_201_CREATED,
)
async def add_user(
    user: User
) -> Response:

    is_user_exist = User.user_name == user.user_name

    existing_user = await user.find_one(
        is_user_exist,
    )

    if existing_user is not None:
        raise users_exceptions.UserAlreadyExists(
            user_name=user.user_name,
        )

    user.password = Hash.get_password_hash(
        password=user.password,
    )

    await user.create()

    return Response(
        status_code=status.HTTP_201_CREATED,
        message=f'User {user.user_name} created succefully',
    )


@ router.get(
    path='/',
    status_code=status.HTTP_200_OK,
    response_description='Get all Users',
    response_model_exclude_none=True,
)
async def get_all_users(
) -> Response:

    users = await User.find_all(
        projection_model=ShowUser,
    ).to_list()

    return Response(
        status_code=status.HTTP_200_OK,
        message='Succefully fetched all users',
        data=users,
        additional_info={
            'count': len(users)
        }
    )


@ router.get(
    path='/{id}',
    status_code=status.HTTP_200_OK,
    response_description='Get one User by id',
    response_model_exclude_none=True,
)
async def get_user_by_id(
    id: PydanticObjectId,
) -> Response:

    is_user_exist = User.id == id

    user = await User.find_one(
        is_user_exist,
        projection_model=ShowUser,
    )

    if user is None:
        raise users_exceptions.UserDoesNotExist(
            id=str(id),
        )

    return Response(
        status_code=status.HTTP_200_OK,
        message=f'Succefully fetched user with id {id}',
        data=user,
    )
