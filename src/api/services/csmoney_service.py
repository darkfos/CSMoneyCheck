from src.api.dto.cs_money_dto import MoneyItemsData
from src.api.exceptions.enum_for_excp import ServiceErrors
from src.cs_services.cs_money_parse import CSMoneyParse
from src.api.exceptions.market_exception import MarketException
from typing import Union


class CSMoneyService:

    async def get_items_data(self, item_name: str) -> MoneyItemsData:

        items_data: Union[bool, dict] = CSMoneyParse().get_all_data_by_itemname(  # noqa
            item_name=item_name
        )

        if items_data:
            return MoneyItemsData(
                count=items_data["count"],
                items=[item for item in items_data.get("items")],
            )

        await MarketException.not_found_a_items(
            txt_for_detail=ServiceErrors.cs_money.value
        )
