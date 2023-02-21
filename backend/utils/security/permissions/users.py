from fastapi import Depends, HTTPException
from utils.security.auth import Auth

from models.user import User, Role


class UserRoleChecker:
    def __init__(self, allowed_roles: list[Role]) -> None:
        self.allowed_roles = allowed_roles

    def __call__(self, user: User = Depends(Auth.get_current_user)) -> None:
        msg = f'User with role {user.role.value} not permited to perform operation'

        if user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=403,
                detail=msg,
            )


allowed_to_post = UserRoleChecker(
    allowed_roles=[Role.CREATOR, Role.ADMIN]
)
allowed_to_get = UserRoleChecker(
    allowed_roles=[Role.CREATOR, Role.VIEWER, Role.ADMIN]
)
allowed_to_delete = UserRoleChecker(
    allowed_roles=[Role.CREATOR, Role.ADMIN]
)

allowed_to_update = UserRoleChecker(
    allowed_roles=[Role.CREATOR, Role.ADMIN]
)
