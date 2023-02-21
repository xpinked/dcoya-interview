from fastapi import HTTPException, status
from models.response import Response


class PostAlreadyExists(
    HTTPException
):
    '''Post already exists exception'''

    def __init__(self) -> None:
        response = Response(
            status_code=status.HTTP_400_BAD_REQUEST,
            message='Post already exists',
        )

        super().__init__(
            status_code=response.status_code,
            detail=response.dict(
                exclude_none=True
            ),
        )


class PostDoesNotExist(
    HTTPException
):
    '''Post does not exist exception'''

    def __init__(self) -> None:
        response = Response(
            status_code=status.HTTP_404_NOT_FOUND,
            message='Post does not exist or removed',
        )

        super().__init__(
            status_code=response.status_code,
            detail=response.dict(
                exclude_none=True
            ),
        )


class PostDeletionNotAllowed(
    HTTPException
):
    '''Current user not allowed to delete post'''

    def __init__(self) -> None:
        response = Response(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message='Current user not allowed to delete post',
        )

        super().__init__(
            status_code=response.status_code,
            detail=response.dict(
                exclude_none=True
            ),
        )


class PostUpdateNotAllowed(
    HTTPException
):
    '''Current user not allowed to update post'''

    def __init__(self) -> None:
        response = Response(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message='Current user not allowed to update post',
        )

        super().__init__(
            status_code=response.status_code,
            detail=response.dict(
                exclude_none=True
            ),
        )
