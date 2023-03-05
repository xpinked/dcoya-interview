import asyncio
import pytest
import pytest_asyncio

import main

from fastapi import FastAPI
from httpx import AsyncClient
from asgi_lifespan import LifespanManager


@pytest.fixture(scope="session")
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def test_app():

    app = main.get_app(
        database_client=main.beanie_client,
        database_name='test_db',
    )

    yield app


@pytest_asyncio.fixture
async def app(test_app: FastAPI):
    async with LifespanManager(test_app):
        yield test_app


@pytest_asyncio.fixture
async def client(app: FastAPI):
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c
