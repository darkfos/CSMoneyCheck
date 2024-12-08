from typing import Annotated
from fastapi import APIRouter, status, Depends, Response

from src.api.dto import FavouriteData
from src.api.auth.auth_service import AuthService
from src.configs.logger_config import logger_dep
from logging import Logger


fav_router: APIRouter = APIRouter(
    prefix="/favourite",
    tags=["Favourites"]
)


@fav_router.post(
    path="/create",
    description="""
    Create favourite item by user
    """,
    summary="Create favourite",
    response_model=None,
    status_code=status.HTTP_201_CREATED
)
async def create_favourite(
        logger: Annotated[Logger, Depends(logger_dep)],
        user_data: Annotated[str, Depends(AuthService.verify_user)],
        response: Response,
        fav_data: FavouriteData
) -> None:
    print(user_data, fav_data)
