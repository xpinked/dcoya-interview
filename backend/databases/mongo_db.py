from beanie import init_beanie
from typing import Optional, Any

from databases.database import DatabaseClient


class BeanieClient(
    DatabaseClient,
):

    def __init__(
        self,
        client,
        models: Optional[list[Any]] = None,
    ) -> None:
        self.client = client

        self.models = models

    async def init_db(
        self,
        database_name: str,
    ) -> None:

        self.database = await self.get_database(database_name)

        await init_beanie(
            database=self.database,
            document_models=self.models
        )

    async def get_collection(
        self,
        collection_name: str,
        database_name: str,
    ):
        return self.client[database_name][collection_name]

    async def get_database(
        self,
        database_name: str,
    ):
        return self.client[database_name]
