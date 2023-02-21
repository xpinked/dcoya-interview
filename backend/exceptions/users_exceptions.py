from fastapi import HTTPException, status
from models.response import Response


class UserAlreadyExists(
    HTTPException
):
    '''User already exists exception'''

    def __init__(self, user_name: str) -> None:
        response = Response(
            status_code=status.HTTP_400_BAD_REQUEST,
            message=f'A User with user_name {user_name} already exists',
        )

        super().__init__(
            status_code=response.status_code,
            detail=response.dict(
                exclude_none=True
            ),
        )


class UserDoesNotExist(
    HTTPException
):
    '''User does not exist exception'''

    def __init__(self, id: str) -> None:
        response = Response(
            status_code=status.HTTP_404_NOT_FOUND,
            message=f'A User with id {id} does not exist',
        )

        super().__init__(
            status_code=response.status_code,
            detail=response.dict(
                exclude_none=True
            ),
        )
