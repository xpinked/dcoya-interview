import uvicorn

from app import get_app
from configurations.config import settings

app = get_app()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG,
        port=settings.PORT,
        access_log=False,
    )
