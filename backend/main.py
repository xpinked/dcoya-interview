import motor.motor_asyncio
import uvicorn

import models

from my_app import get_app
from configurations.config import settings
from databases import BeanieClient


beanie_client = BeanieClient(
    client=motor.motor_asyncio.AsyncIOMotorClient(
        host=settings.MONGO_HOST,
        port=settings.MONGO_PORT,
        username=settings.MONGO_USER,
        password=settings.MONGO_PASSWORD,
    ),
    models=[
        models.post.Post,
        models.user.User,
        models.like.Like,
    ],
)

app = get_app(
    database_client=beanie_client,
    database_name=settings.MONGO_DB_NAME,
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG,
        port=settings.PORT,
        access_log=False,
        workers=4,
    )
