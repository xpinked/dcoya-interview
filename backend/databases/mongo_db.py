import models
import motor.motor_asyncio

from beanie import init_beanie

from configurations.config import settings


class MongoDBClient:
    client = motor.motor_asyncio.AsyncIOMotorClient(
        host=settings.MONGO_HOST,
        port=settings.MONGO_PORT,
        username=settings.MONGO_USER,
        password=settings.MONGO_PASSWORD,
    )

    document_models = [
        models.post.Post,
        models.user.User,
        models.like.Like,
    ]

    @classmethod
    async def init_db(
        cls,
    ) -> None:

        database = cls.client[settings.MONGO_DB_NAME]

        await init_beanie(
            database=database,
            document_models=cls.document_models
        )

    @classmethod
    def get_collection(
        cls,
        collection_name: str,
        database_name: str = settings.MONGO_DB_NAME,
    ):
        return cls.client[database_name][collection_name]

    @classmethod
    def get_database(
        cls,
        database_name: str = settings.MONGO_DB_NAME,
    ):
        return cls.client[database_name]
