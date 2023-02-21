from pydantic import BaseModel


class AuthDetails(BaseModel):
    user_name: str
    password: str

    class Config:
        anystr_strip_whitespace = True
        schema_extra = {
            'example': {
                'user_name': 'Israeli123',
                'password': 'VerySecretPassword',
            }
        }
