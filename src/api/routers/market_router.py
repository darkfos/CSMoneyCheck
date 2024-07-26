from fastapi import APIRouter, status
from src.api.services.market_service import MarketService, MarketItemsData


market_router: APIRouter = APIRouter(
    prefix="/market",
    tags=["Market"],
)


@market_router.get(
    path="/get_data_about_item",
    status_code=status.HTTP_200_OK,
    description="Получение информации о предметах",
    response_model=MarketItemsData
    )
async def get_item_from_market(
    item: str
):
    data = await MarketService().get_items_data(item_name=item)
    print(data)
    return data