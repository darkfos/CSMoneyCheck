from fastapi import APIRouter, status
from src.api.services.market_service import MarketService, MarketItemsData


market_router: APIRouter = APIRouter(
    prefix="/market",
    tags=["Market"],
)


@market_router.get(
    path="/get_items",
    status_code=status.HTTP_200_OK,
    description="Получение информации о предметах",
    response_model=MarketItemsData
    )
async def get_items_data_market(
    item: str
):
    data = await MarketService().get_items_data(item_name=item)
    return data