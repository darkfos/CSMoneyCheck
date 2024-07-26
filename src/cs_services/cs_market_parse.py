from requests import Session
from typing import Union
import asyncio
import json
from bs4 import BeautifulSoup as bs_engine


class CSMarketParse:

    def __init__(self) -> None:
        self.__parse_url: str = "https://market.csgo.com/api/graphql"
        self.session: Session = Session()
    
    async def search_item(self, item_name: str) -> None:
        """
        Получение всех item's
        :item_name:
        """

        query_data: dict = {
        "operationName": "items",
        "variables": {
            "filters": [
                {
                    "id": "search",
                    "items": [
                        {
                            "id": item_name
                        }
                    ]
                }
            ],
            "order": {
                "id": "default",
                "direction": "desc"
            },
            "offset": 0,
            "count": 498
        },
        "query": """query items($count: Int, $filters: [FilterInputType], $page: Int, $offset: Int, $order: OrderInputType!) {
        items(
            count: $count
            filters: $filters
            page: $page
            order: $order
            offset: $offset
        ) {
            paginatorInfo {
            count
            currentPage
            hasMorePages
            lastPage
            perPage
            total
            __typename
            }
            filters {
            id
            items {
                color
                id
                name
                plural
                icons
                items {
                color
                id
                name
                icons
                __typename
                }
                __typename
            }
            min_value
            max_value
            min_range
            max_range
            min
            max
            step
            name
            order
            type
            value
            open
            __typename
            }
            meta {
            title
            description
            __typename
            }
            data {
            color
            id
            currency
            stattrak
            slot
            popularity
            features
            rarity
            my_item
            rarity_ext {
                id
                name
                __typename
            }
            ctp
            quality
            phase
            descriptions {
                type
                value
                __typename
            }
            type
            tags {
                category
                category_name
                localized_category_name
                localized_tag_name
                internal_name
                name
                value {
                name
                link
                __typename
                }
                __typename
            }
            image_512
            image_100
            image_150
            image_300
            seo {
                category
                type
                __typename
            }
            market_hash_name
            market_name
            price
            stickers {
                image
                name
                __typename
            }
            __typename
            }
            paginatorInfo {
            count
            currentPage
            hasMorePages
            lastPage
            perPage
            total
            __typename
            }
            __typename
        }
        }"""
}       
        url_to_referer: str = self.session.get(url=f"https://market.csgo.com/ru/?search={item_name}").url.split("=")[-1]
        req = self.session.post(
            self.__parse_url,
            headers={
                "Accept": "application/json, text/plain, */*",
                "App-Settings": "lang=ru",
                "Content-Type": "application/json",
                "Referer": f"https://market.csgo.com/ru/?search={url_to_referer}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36"
                },
            data=json.dumps(query_data)
        )

        if req.status_code == 200:
            with open("src/cs_services/js_data_items/csmarket.json", "w", encoding="UTF-8") as file:
                json.dump(req.json(), file, indent=4)
            return True
        return False
    
    async def get_all_data_by_itemname(self, item_name: str) -> Union[dict[str, Union[str, int]], bool]:
        """
        Поиск предметов по названию
        :item_name:
        """

        is_saved: bool = await self.search_item(item_name=item_name)

        if is_saved: 
            
            #Open file
            with open("src/cs_services/js_data_items/csmarket.json", "r") as file:
                file_data: dict = json.load(file)

                data_to_response: dict = {
                    "count": file_data["data"]["items"]["paginatorInfo"]["count"],
                    "items": [
                        {
                            "currency": item["currency"],
                            "rarity": item["rarity"],
                            "name": item["rarity_ext"]["name"],
                            "market_hash_name": item["market_hash_name"],
                            "quality": item["quality"],
                            "stickers": item["stickers"],
                            "price": item["price"]
                        }
                        for item in file_data["data"]["items"]["data"]
                    ]
                }

                return data_to_response
        else: return False

cs_money_parse_object: CSMarketParse = CSMarketParse()
asyncio.run(cs_money_parse_object.get_all_data_by_itemname("sdsd"))