from src.api.dto import MoneyItemsData
from src.api.exceptions import ServiceErrors
from src.cs_services import CSMoneyParse
from src.api.exceptions import MarketException
from typing import Union


class CSMoneyService:

    async def get_items_data(self, item_name: str) -> MoneyItemsData:

        items_data: Union[bool, dict] = CSMoneyParse().get_all_data_by_itemname(  # noqa
            item_name=item_name
        )

        print(items_data)

        if items_data:
            return MoneyItemsData(
                count=items_data["count"],
                items=[item for item in items_data.get("items")],
            )

        await MarketException.not_found_a_items(
            txt_for_detail=ServiceErrors.cs_money.value
        )
