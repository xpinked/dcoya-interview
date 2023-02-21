from fastapi import HTTPException, status
from models.response import Response


class LikeAlreadyExists(
    HTTPException
):
    '''Like already exists exception'''

    def __init__(self) -> None:
        response = Response(
            status_code=status.HTTP_400_BAD_REQUEST,
            message='Like already exists',
        )

        super().__init__(
            status_code=response.status_code,
            detail=response.dict(
                exclude_none=True
            ),
        )


class LikeDoesNotExist(
    HTTPException
):
    '''Like does not exist exception'''

    def __init__(self) -> None:
        response = Response(
            status_code=status.HTTP_404_NOT_FOUND,
            message='Like does not exist',
        )

        super().__init__(
            status_code=response.status_code,
            detail=response.dict(
                exclude_none=True
            ),
        )


class NotAllowedToRemoveLike(
    HTTPException
):
    '''User Not allowed to like exception'''

    def __init__(self) -> None:
        response = Response(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message='You are not allowed to remove this user like',
        )

        super().__init__(
            status_code=response.status_code,
            detail=response.dict(
                exclude_none=True
            ),
        )
