import json
from typing import Annotated
from fastapi import APIRouter, status, Depends, Response
from pydantic.v1.typing import Any

from src.api.dto import FavouriteData
from src.api.auth.auth_service import AuthService
from src.configs import user_config
from src.configs.logger_config import logger_dep
from src.api.services.favourite_service import FavouriteService  # noqa
from src.enums_cs import APIRouterTagsEnum, APIRouterPrefixEnum  # noqa
from src.api import redis
from src.database.redis.redis_worker import RedisWorker  # noqa
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
    """
    Create user favourite
    :param logger:
    :param user_data:
    :param response:
    :param fav_data:
    :return:
    """

    logger.info(
        msg=f"FAVOURITE: User add item: {fav_data.items}", extra=user_config
    )  # noqa

    return await FavouriteService.create_row_in_fav_collection(
        data=fav_data, token_data=user_data
    )


@fav_router.get(
    path="/favourites",
    description="""All user favourites""",
    summary="All favourites",
    response_model=Any,
    status_code=status.HTTP_200_OK,
)  # noqa
async def my_favourites(
    logger: Annotated[Logger, Depends(logger_dep)],
    user_data: Annotated[dict, Depends(AuthService.verify_user)],
    response: Response,
    redis: Annotated[RedisWorker, Depends(redis)],
) -> Any:
    """
    All user favourites
    :param logger:
    :param user_data:
    :param response:
    :param redis:
    :return:
    """

    logger.info(
        msg=f"FAVOURITE: Get all favourites by id_user={user_data.get("sub")}",
        extra=user_config,
    )  # noqa
    redis_req = await redis.get_value(key=f"my_fav_{user_data.get("sub")}")

    if redis_req:
        return redis_req

    user_fav = await FavouriteService.get_my_favourites(token_data=user_data)
    await redis.set_key(
        key=f"my_fav_{user_data.get("sub")}", value=json.dumps(user_fav)
    )
    return user_fav


@fav_router.delete(
    path="/delete",
    description="""
    Delete favourite user by id
    """,
    summary="Delete favourite",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_fav(
    logger: Annotated[Logger, Depends(logger_dep)],
    user_data: Annotated[str, Depends(AuthService.verify_user)],
    response: Response,
    id_fav: str,
) -> None:
    """
    Delete favourite user by id
    :param logger:
    :param user_data:
    :param response:
    :param id_fav:
    :return:
    """

    logger.info(
        msg=f"FAVOURITE: Delete favourite by id={id_fav}", extra=user_config
    )  # noqa

    return await FavouriteService.delete_fav(
        token_data=user_data, id_fav=id_fav
    )  # noqa
