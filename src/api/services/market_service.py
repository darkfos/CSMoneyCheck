from src.api.dto.cs_market_dto import MarketItemsData
from src.cs_services.cs_market_parse import CSMarketParse
from src.api.exceptions.market_exception import MarketException


class MarketService:

    async def get_items_data(self, item_name: str) -> MarketItemsData:
        """
        Получение всей информации о предметах
        :item_name:
        """

        item_data: dict = await CSMarketParse().get_all_data_by_itemname(item_name=item_name)
        if item_data.get("items") != []:
            print(item_data["items"])
            return MarketItemsData(
                count=item_data.get("count"),
                items=[itm for itm in item_data.get("items")]
            )
        await MarketException.not_found_a_items()