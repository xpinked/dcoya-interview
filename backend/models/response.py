from pydantic import Field, BaseModel
from typing import Optional, Any


class Response(BaseModel):

    status_code: int = Field(
        ...,
        description='HTTP status code'
    )

    message: Optional[str] = Field(
        default=None,
        description='Response message'
    )

    data: Optional[Any] = Field(
        default=None,
        description='Data to attache'
    )

    additional_info: Optional[dict] = Field(
        default=None,
        description='Additonal info'
    )
