import pytest

from fastapi import status

from httpx import AsyncClient, Response

test_users = {
    'default': {
        '_id': '6403deecee6c7140129e333b',
        'name': 'Israel Default',
        'user_name': 'Israeli123',
        'password': 'password',
        'role': 'viewer',
    },
    'admin': {
        '_id': '6403e0f40ec322a7aba3c3a6',
        'name': 'Israel Admin',
        'user_name': 'Israeli123',
        'password': 'password',
        'role': 'admin',
    },
    'creator': {
        '_id': '6403e16ecd1dd5d46d2c0548',
        'name': 'Israel Creator',
        'user_name': 'Israeli123',
        'password': 'password',
        'role': 'creator',
    },
    'viewer': {
        '_id': '6403e19f13cb6d6dca7a60e1',
        'name': 'Israel viewer',
        'user_name': 'Israeli123',
        'password': 'password',
        'role': 'viewer',
    },
}


async def create_test_user(
    client: AsyncClient,
    user: dict[str, str] = test_users['default'],
) -> Response:

    response = await client.post(
        url='/api/v1/users/',
        json=user,
    )

    return response


@pytest.mark.asyncio
async def test_get_create_user(client: AsyncClient) -> None:

    response = await create_test_user(client)

    assert response.status_code == status.HTTP_201_CREATED

    response_body = response.json()

    assert response_body['data']['_id'] == '6403deecee6c7140129e333b'


@pytest.mark.asyncio
async def test_get_all_users(client: AsyncClient) -> None:

    response = await client.get('/api/v1/users/')

    assert response.status_code == status.HTTP_200_OK

    response_body = response.json()

    data = response_body.get('data')

    assert isinstance(data, list) and len(data) >= 0


@pytest.mark.asyncio
async def test_user_already_created(client: AsyncClient) -> None:

    response = await create_test_user(client)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio
async def test_get_user_by_id(client: AsyncClient) -> None:

    default_user_id = test_users['default']['_id']

    response = await client.get(
        url=f"/api/v1/users/{default_user_id}",
    )

    assert response.status_code == status.HTTP_200_OK

    response_data = response.json().get('data')

    assert response_data is not None

    fetched_user_id = response_data.get('_id')

    assert fetched_user_id == default_user_id
