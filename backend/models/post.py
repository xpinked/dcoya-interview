from datetime import datetime

from beanie import Document, PydanticObjectId
from pydantic import Field, BaseModel
from typing import Optional


class Post(Document):
    title: str = Field(
        ...,
        description='Post Title'
    )

    content: str = Field(
        ...,
        description='Post body content, must have at 2 to 1000 characters',
        min_length=2,
        max_length=1000,
    )

    creator_id: Optional[PydanticObjectId] = Field(
        description='Post creator id'
    )

    creation_date: Optional[datetime] = Field(
        default_factory=datetime.now,
        description='post creation date'
    )

    update_date: Optional[datetime] = creation_date

    class Settings:
        name = 'posts'

    class Config:
        anystr_strip_whitespace = True
        schema_extra = {
            'example': {
                'title': 'Israel Post',
                'content': 'My long content.....',
            }
        }


class UpdatePost(BaseModel):
    title: Optional[str] = Field(
        description='Post updated title'
    )

    content: Optional[str] = Field(
        description='Post updated content',
        min_length=1,
        max_length=1000,
    )

    update_date: datetime = Field(
        default_factory=datetime.now,
        description='Post update date'
    )

    class Config:
        anystr_strip_whitespace = True
        schema_extra = {
            'example': {
                'title': 'My Updated Post Title',
                'content': 'My updated content',
            }
        }
