import json
from logging import Logger
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from src.api.auth.auth_service import AuthService
from src.configs.logger_config import logger_dep, user_config
from src.cs_services import ProfileService
from src.enums_cs.api_router_enums import APIRouterTagsEnum, APIRouterPrefixEnum  # noqa
from src.api import redis
from src.database.redis.redis_worker import RedisWorker  # noqa
from typing import Final, Annotated, List


profile_router: Final[APIRouter] = APIRouter(
    prefix=APIRouterPrefixEnum.PROFILE_PREFIX.value,
    tags=APIRouterTagsEnum.PROFILE_TAGS.value,
)


@profile_router.get(
    path="/profile_steam_items_data",
    description="""Получение информации о инвентаре steam профиля""",
    response_model=List[dict],
    summary="Инвентарь пользователя",
    status_code=status.HTTP_200_OK,
)
async def profile_items_data(
    logger: Annotated[Logger, Depends(logger_dep)],
    redis: Annotated[RedisWorker, Depends(redis)],
    user_data: Annotated[dict, Depends(AuthService.verify_user)],
    profile_id: int,
) -> List[dict]:
    """
    APIROUTER Profile: get items data (inventory user)
    """

    logger.info(
        msg="Получение данных о инвентаре пользователя", extra=user_config
    )  # noqa
    redis_data = await redis.get_value(
        key="profile_data_{}".format(user_data.get("sub"))
    )

    if redis_data:
        return redis_data

    req = await ProfileService.get_inventory_data(profile_id=profile_id)
    if not req:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No found user profile",  # noqa
        )

    await redis.set_key(
        key="profile_data_{}".format(user_data.get("sub")),
        value=json.dumps(req),  # noqa
    )  # noqa
    return req


@profile_router.get(
    path="/item_data",
    description="Получение информации о предмете",
    response_model=dict,
    summary="Информация о предмете",
    status_code=status.HTTP_200_OK,
)
async def item_data(
    logger: Annotated[Logger, Depends(logger_dep)],
    redis: Annotated[RedisWorker, Depends(redis)],
    item_name: str,
) -> dict:
    """
    APIROUTER Profile: get item data

    :param logger:
    :param redis:
    :param item_name:
    """

    logger.info(msg="Получение данных о предмете", extra=user_config)
    redis_data = await redis.get_value(key="item_data_{}".format(item_name))

    if redis_data:
        return redis_data

    req = await ProfileService.get_item_data(market_hash_name=item_name)
    if not req:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No found item"
        )

    await redis.set_key(
        key="item_data_{}".format(item_name), value=json.dumps(req)
    )  # noqa
    return req
