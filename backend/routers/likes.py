import exceptions.likes_exceptions as likes_exceptions
import exceptions.posts_exceptions as posts_exceptions

from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, status

from models.user import UserData
from models.like import Like
from models.post import Post
from models.response import Response

from utils.security.auth import Auth

router = APIRouter()


@router.post(
    path='/{post_id}',
    response_description='Add like to post by ID',
    response_model_exclude_none=True,
    status_code=status.HTTP_201_CREATED,
)
async def add_like_by_post_id(
    post_id: PydanticObjectId,
    current_user: UserData = Depends(Auth.get_current_user),
) -> Response:

    current_user_id = PydanticObjectId(current_user.id)

    existing_post = await Post.find_one(
        Post.id == post_id,
    )

    if existing_post is None:
        raise posts_exceptions.PostDoesNotExist()

    existing_like = await Like.find_one(
        Like.doc_reference_id == post_id,
        Like.liked_by == current_user_id,
    )

    if existing_like is not None:
        raise likes_exceptions.LikeAlreadyExists()

    like = Like(
        liked_by=current_user_id,
        doc_reference_id=post_id,
    )

    await like.create()

    return Response(
        status_code=status.HTTP_201_CREATED,
        message=f'Like for post {like.doc_reference_id} added succefully',
        data=like,
    )


@router.delete(
    path='/{post_id}',
    response_description='Remove like to post by ID',
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK,
)
async def remove_like_by_post_id(
    post_id: PydanticObjectId,
    current_user: UserData = Depends(Auth.get_current_user),
) -> Response:

    current_user_id = PydanticObjectId(current_user.id)

    existing_post = await Post.find_one(
        Post.id == post_id,
    )

    if existing_post is None:
        raise posts_exceptions.PostDoesNotExist()

    existing_like = await Like.find_one(
        Like.doc_reference_id == post_id,
        Like.liked_by == current_user_id,
    )

    if existing_like is None:
        raise likes_exceptions.LikeDoesNotExist()

    if existing_like.liked_by != current_user_id:
        raise likes_exceptions.NotAllowedToRemoveLike()

    await existing_like.delete()

    return Response(
        status_code=status.HTTP_201_CREATED,
        message=f'Like for post {post_id} removed succefully',
        data=existing_like,
    )


@router.get(
    path='/{post_id}',
    response_description='Get all likes for post by ID',
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK,
)
async def gets_likes_by_post_id(
    post_id: PydanticObjectId,
    current_user: UserData = Depends(Auth.get_current_user),
) -> Response:

    existing_post = await Post.get(post_id)

    if existing_post is None:
        raise posts_exceptions.PostDoesNotExist()

    is_post_having_likes =  \
        Like.doc_reference_id == post_id

    likes = await Like.find_many(
        is_post_having_likes,
    ).to_list()

    return Response(
        status_code=status.HTTP_201_CREATED,
        message=f'Fetched likes for post with id {post_id}',
        data=likes,
        additional_info={
            'count': len(likes)
        }
    )
