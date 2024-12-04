from fastapi import APIRouter, status, Depends
from typing import Annotated
from logging import Logger
from src.api.services import CSMoneyService
from src.api.dto import MoneyItemsData
from src.configs import user_config, logger_dep


cs_money_router: APIRouter = APIRouter(prefix="/cs_money", tags=["CSMoney"])


@cs_money_router.get(
    path="/get_items",
    description="Получение данных о всех предметах",
    response_model=MoneyItemsData,
    status_code=status.HTTP_200_OK,
)
async def get_items_data_cs_money(
    logger: Annotated[Logger, Depends(logger_dep)], item_name: str
) -> MoneyItemsData:
    """
    Получение полной информации о предметах по названию из сервиса
    CSMoney
    :param logger:
    :param item_name:
    :return:
    """

    logger.info(msg="CSMONEY: Получение предмета = %s" % item_name, extra=user_config) # noqa
    return await CSMoneyService().get_items_data(item_name=item_name)
