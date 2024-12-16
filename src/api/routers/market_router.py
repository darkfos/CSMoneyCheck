from fastapi import APIRouter, status, Depends, Response

from src.api.auth.auth_service import AuthService
from src.api.services import MarketService, MarketItemsData
from typing import Annotated
from logging import Logger
from src.configs import user_config, logger_dep
from src.enums_cs import APIRouterTagsEnum, APIRouterPrefixEnum  # noqa
from src.api import redis, RedisWorker


market_router: APIRouter = APIRouter(
    prefix=APIRouterPrefixEnum.MARKET_PREFIX.value,
    tags=APIRouterTagsEnum.MARKET_TAGS.value,
)


@market_router.get(
    path="/get_items",
    status_code=status.HTTP_200_OK,
    description="Получение информации о предметах",
    response_model=MarketItemsData,
)
async def get_items_data_market(
    logger: Annotated[Logger, Depends(logger_dep)],
    redis_db: Annotated[RedisWorker, Depends(redis)],
    auth: Annotated[str, Depends(AuthService.verify_user)],  # noqa
    response: Response,
    item: str,
):
    """
    Получение информации о всех предметах по названию из Market
    :param logger:
    :param item:
    :return:
    """

    logger.info(msg="MARKET: Получение предмета=%s" % item, extra=user_config)

    redis_data = await redis_db.get_value(key=item)
    if redis_data:
        return redis_data
    else:
        data = await MarketService().get_items_data(item_name=item)
        await redis_db.set_key(key=item, value=data.json())
        return data
