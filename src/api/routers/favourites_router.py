from typing import Annotated
from fastapi import APIRouter, status, Depends, Response

from src.api.dto import FavouriteData
from src.api.auth.auth_service import AuthService
from src.configs.logger_config import logger_dep
from src.api.services.favourite_service import FavouriteService  # noqa
from src.enums_cs import APIRouterTagsEnum, APIRouterPrefixEnum  # noqa
from logging import Logger


fav_router: APIRouter = APIRouter(
    prefix=APIRouterPrefixEnum.FAVOURITE_PREFIX.value,
    tags=APIRouterTagsEnum.FAVOURITE_TAGS.value,
)


@fav_router.post(
    path="/create",
    description="""
    Create favourite item by user
    """,
    summary="Create favourite",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
async def create_favourite(
    logger: Annotated[Logger, Depends(logger_dep)],
    user_data: Annotated[dict, Depends(AuthService.verify_user)],
    response: Response,
    fav_data: FavouriteData,
) -> None:

    logger.info(msg=f"FAVOURITE: User add item: {fav_data.items}")

    return await FavouriteService.create_row_in_fav_collection(
        data=fav_data, token_data=user_data
    )
