import exceptions.posts_exceptions as posts_exceptions
import utils.security.permissions.users as permissions

from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, status

from models.post import Post, UpdatePost
from models.response import Response
from models.user import UserData
from utils.security.auth import Auth


router = APIRouter()


@router.post(
    path='/',
    response_description='Create new Post',
    response_model_exclude_none=True,
    status_code=status.HTTP_201_CREATED,
    dependencies=[
        Depends(permissions.allowed_to_post)
    ],
)
async def add_new_post(
    post: Post,
    current_user: UserData = Depends(Auth.get_current_user),
) -> Response:

    current_user_id = PydanticObjectId(current_user.id)

    is_post_exist = Post.title == post.title

    existing_post = await post.find_one(
        is_post_exist,
    )

    if existing_post is not None:
        raise posts_exceptions.PostAlreadyExists()

    if current_user.id is None:
        raise Auth.credentials_exception

    post.creator_id = current_user_id

    await post.create()

    return Response(
        status_code=status.HTTP_201_CREATED,
        message='Post created succefully',
    )


@router.get(
    path='/',
    status_code=status.HTTP_200_OK,
    response_description='Get all posts',
    response_model_exclude_none=True,
    dependencies=[
        Depends(permissions.allowed_to_get)
    ]
)
async def get_all_posts(
    current_user: UserData = Depends(Auth.get_current_user)
) -> Response:

    posts = await Post.find_all(
        # projection_model=ShowPost,
    ).to_list()

    return Response(
        status_code=status.HTTP_200_OK,
        message='Succefully fetched all posts',
        data=posts,
        additional_info={
            'count': len(posts)
        }
    )


@router.get(
    path='/{id}',
    status_code=status.HTTP_200_OK,
    response_description='Get one Post by id',
    response_model_exclude_none=True,
    dependencies=[
        Depends(permissions.allowed_to_get)
    ],
)
async def get_post_by_id(
    id: PydanticObjectId,
    current_user: UserData = Depends(Auth.get_current_user),
) -> Response:

    post = await Post.get(id)

    if post is None:
        raise posts_exceptions.PostDoesNotExist()

    return Response(
        status_code=status.HTTP_200_OK,
        message=f'Succefully fetched Post with id {id}',
        data=post,
    )


@router.delete(
    path='/{id}',
    status_code=status.HTTP_200_OK,
    response_description='Delete one Post by id',
    response_model_exclude_none=True,
    dependencies=[
        Depends(permissions.allowed_to_delete)
    ]
)
async def delete_post_by_id(
    id: PydanticObjectId,
    current_user: UserData = Depends(Auth.get_current_user),
) -> Response:

    current_user_id = PydanticObjectId(current_user.id)

    post = await Post.get(id)

    if post is None:
        raise posts_exceptions.PostDoesNotExist()

    if post.creator_id != current_user_id:
        raise posts_exceptions.PostDeletionNotAllowed()

    await post.delete()

    return Response(
        status_code=status.HTTP_200_OK,
        message=f'Succefully deleted Post with id {id}',
    )


@router.put(
    path='/{id}',
    status_code=status.HTTP_200_OK,
    response_description='Delete one Post by id',
    response_model_exclude_none=True,
    dependencies=[
        Depends(permissions.allowed_to_update)
    ]
)
async def update_post_by_id(
    id: PydanticObjectId,
    updated_post: UpdatePost,
    current_user: UserData = Depends(Auth.get_current_user),
) -> Response:

    if current_user.id is None:
        raise Auth.credentials_exception

    existing_post = await Post.get(id)

    if existing_post is None:
        raise posts_exceptions.PostDoesNotExist()

    if existing_post.creator_id != PydanticObjectId(current_user.id):
        raise posts_exceptions.PostUpdateNotAllowed()

    existing_post_with_same_title = await Post.find_one(
        Post.title == updated_post.title
    )

    if existing_post_with_same_title is not None:
        raise posts_exceptions.PostAlreadyExists()

    updated_post_dict = updated_post.dict(
        exclude_none=True
    )

    await existing_post.set(
        expression=updated_post_dict
    )

    return Response(
        status_code=status.HTTP_200_OK,
        message=f'Succefully updated Post with id {id}',
        data=existing_post,
    )
