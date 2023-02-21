from datetime import datetime

from beanie import Document, PydanticObjectId
from pydantic import Field
from typing import Optional


class Like(Document):

    doc_reference_id: PydanticObjectId = Field(
        ...,
        description='A document reference id to like'
    )

    liked_by: PydanticObjectId = Field(
        ...,
        description='The users ID who liked the document'
    )

    creation_date: Optional[datetime] = Field(
        default_factory=datetime.now,
        description='Like creation date'
    )

    class Settings:
        name = 'likes'

    class Config:
        anystr_strip_whitespace = True
        schema_extra = {
            'example': {
                'doc_reference_id': '62839ad1d9a88a040663a734',
                'liked_by': '62839ad1d9a88a040663a734',
            }
        }
