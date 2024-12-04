from fastapi import APIRouter, status, Depends
from src.api.services.market_service import MarketService, MarketItemsData
from typing import Annotated
from logging import Logger
from src.configs import user_config, logger_dep


market_router: APIRouter = APIRouter(
    prefix="/market",
    tags=["Market"],
)


@market_router.get(
    path="/get_items",
    status_code=status.HTTP_200_OK,
    description="Получение информации о предметах",
    response_model=MarketItemsData,
)
async def get_items_data_market(
    logger: Annotated[Logger, Depends(logger_dep)],
    item: str
):
    """
    Получение информации о всех предметах по названию из Market
    :param logger:
    :param item:
    :return:
    """

    logger.info(msg="MARKET: Получение предмета=%s"%item, extra=user_config)
    data = await MarketService().get_items_data(item_name=item)
    return data
