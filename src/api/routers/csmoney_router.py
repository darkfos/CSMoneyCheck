from fastapi import APIRouter, status
from src.api.services.csmoney_service import CSMoneyService
from src.api.dto.cs_money_dto import MoneyItemsData


cs_money_router: APIRouter = APIRouter(
    prefix="/cs_money",
    tags=["CSMoney"]
)


@cs_money_router.get(
    path="/get_items",
    description="Получение данных о всех предметах",
    response_model=MoneyItemsData,
    status_code=status.HTTP_200_OK
)
async def get_items_data_cs_money(
    item_name: str
) -> MoneyItemsData:
    
    return await CSMoneyService().get_items_data(item_name=item_name)