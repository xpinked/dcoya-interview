import enum
from datetime import datetime

from beanie import Document, PydanticObjectId
from pydantic import BaseModel, Field
from typing import Optional


class Role(
    str,
    enum.Enum
):
    VIEWER = 'viewer'
    CREATOR = 'creator'
    ADMIN = 'admin'


class User(Document):
    name: str = Field(
        ...,
        description='Users name'
    )

    user_name: str = Field(
        ...,
        description='Users UserName',
    )

    password: str = Field(
        ...,
        description='Users password, minimum 8 digits required',
        min_length=8,
    )

    creation_date: Optional[datetime] = Field(
        default_factory=datetime.now,
        description='Users Creation Date'
    )

    role: Role = Field(
        default=Role.VIEWER,
        description='User role'
    )

    class Settings:
        name = 'users'

    class Config:
        anystr_strip_whitespace = True
        schema_extra = {
            'example': {
                'name': 'Israel Israeli',
                'user_name': 'Israeli123',
                'password': 'VerySecretPassword',
                'role': 'creator'
            }
        }


class UserData(BaseModel):
    id: str
    name: str
    user_name: str
    role: Role


class ShowUser(BaseModel):
    id: PydanticObjectId = Field(alias='_id')
    name: str
    user_name: str
    role: Role
