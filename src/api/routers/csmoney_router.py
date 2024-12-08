from fastapi import APIRouter, status, Depends, Response
from typing import Annotated
from logging import Logger
from src.api.services import CSMoneyService
from src.api.dto import MoneyItemsData
from src.configs import user_config, logger_dep
from src.api import redis
from src.database import RedisWorker
from src.api.auth.auth_service import AuthService
from src.enums_cs import APIRouterTagsEnum, APIRouterPrefixEnum  # noqa


cs_money_router: APIRouter = APIRouter(
    prefix=APIRouterPrefixEnum.CSMONEY_PREFIX.value,
    tags=APIRouterTagsEnum.CSMONEY_TAGS.value,
)  # noqa


@cs_money_router.get(
    path="/get_items",
    description="Получение данных о всех предметах",
    response_model=MoneyItemsData,
    status_code=status.HTTP_200_OK,
)
async def get_items_data_cs_money(
    logger: Annotated[Logger, Depends(logger_dep)],
    redis_db: Annotated[RedisWorker, Depends(redis)],
    auth: Annotated[str, Depends(AuthService.verify_user)],  # noqa
    response: Response,
    item_name: str,
) -> MoneyItemsData:
    """
    Получение полной информации о предметах по названию из сервиса
    CSMoney
    :param logger:
    :param item_name:
    :return:
    """

    logger.info(
        msg="CSMONEY: Получение предмета = %s" % item_name, extra=user_config
    )  # noqa

    redis_search_data = await redis_db.get_value(key=item_name)

    if redis_search_data:
        return redis_search_data
    else:
        result = await CSMoneyService().get_items_data(item_name=item_name)
        await redis_db.set_key(key=item_name, value=result.json())
        return result
