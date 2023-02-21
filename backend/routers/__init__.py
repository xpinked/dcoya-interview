from fastapi import APIRouter
from routers import users, likes, posts, authentication

api_routers = APIRouter()

api_routers.include_router(users.router, tags=["Users"], prefix="/users")
api_routers.include_router(posts.router, tags=["Posts"], prefix="/posts")
api_routers.include_router(likes.router, tags=["Likes"], prefix="/likes")
