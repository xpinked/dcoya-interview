import fastapi


from fastapi.middleware.cors import CORSMiddleware

from configurations.config import settings
from databases import DatabaseClient
from middlewares.logger import LoggingMiddleware

from routers import api_routers, authentication


def get_app(
    database_client: DatabaseClient,
    database_name: str,
) -> fastapi.FastAPI:

    app = fastapi.FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(
        LoggingMiddleware,
    )

    app.include_router(
        router=authentication.router,
        prefix='/login',
        tags=['Authentication']
    )

    app.include_router(router=api_routers, prefix='/api/v1')

    @app.on_event("startup")
    async def startup() -> None:
        await database_client.init_db(
            database_name=database_name,
        )

    return app
