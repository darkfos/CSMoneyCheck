from typing import Union, Type
from aiohttp import ClientSession
import json


class CSMoneyParse:

    def __init__(self) -> None:
        self.__url = "https://cs.money/1.0/market/sell-orders"
        self.session: Type[ClientSession] = ClientSession

    async def save_data(self, item_name: str) -> bool:

        async with self.session() as local_session:
            req = await local_session.get(
                url=self.__url,
                params={"limit": 60, "offset": 0, "name": item_name},
                headers={
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br, zstd",
                    "Accept-Language": "ru,en;q=0.9",
                    "Cookie": "region=Rostov Oblast; cc_service2={%22services%22:[%22necessary%22%2C%22gtm%22%2C%22ym%22%2C%22amplitude%22%2C%22gleam%22%2C%22esputnik%22%2C%22hotjar%22%2C%22userSesDatToAnalytic%22%2C%22userSesDatToMarketing%22%2C%22cardVisualSize%22]%2C%22acceptanceDate%22:1721989367417%2C%22revision%22:0%2C%22additionalData%22:{%22country%22:%22RU%22}}; group_id=ada1819a-601e-4f6d-8fb5-23c49ab49cd5; _gcl_au=1.1.793344222.1721989371; sc=EBBFB169-874C-6D49-EEDE-BDB8B2395654; _ym_uid=1721989372385552501; _ym_d=1721989372; _ga=GA1.1.1182838042.1721989372; _hjSessionUser_2848248=eyJpZCI6IjcwMzk5NjU3LWZmNDgtNTIxOS04MmNiLTU4MmUxMTU5YWJlYiIsImNyZWF0ZWQiOjE3MjE5ODkzNzIyODQsImV4aXN0aW5nIjp0cnVlfQ==; _scid=9f44adf9-6397-4cdf-8841-fba67548d767; _ym_isad=2; _sctr=1%7C1721941200000; isAnalyticEventsLimit=true; new_language=ru; cf_clearance=ON76IEPW.fTdLQONtiVPwetdwLUUNgjksbMpHShpoyM-1722024899-1.0.1.1-NDzDpVTya.fv1DX1iA1N3WRPsgWTF_HexgJAwBJ3DgiJ.pMwB.Er9rrV_UmtH2u4xHPrKknMVOKMJ35gGCR8ZA; amplitude_id_c14fa5162b6e034d1c3b12854f3a26f5cs.money=eyJkZXZpY2VJZCI6IjAwYTIxYWY4LWUzYzQtNGYzNC04OWMyLTc3Nzc1NTRmMzc5MFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTcyMjAyNDg5OTkzNCwibGFzdEV2ZW50VGltZSI6MTcyMjAyNDg5OTQwMCwiZXZlbnRJZCI6NywiaWRlbnRpZnlJZCI6Niwic2VxdWVuY2VOdW1iZXIiOjEzfQ==; _hjSession_2848248=eyJpZCI6ImE4Y2FmYzljLWE3MTItNDE1Mi1hOTI4LTQ4NGMyYmQxZDI2ZSIsImMiOjE3MjIwMjQ5MDA5ODIsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _hjHasCachedUserAttributes=true; _ym_visorc=b; settings_visual_card_size=large; u_dpi=1; _scid_r=9f44adf9-6397-4cdf-8841-fba67548d767; _ga_HY7CCPCD7H=GS1.1.1722024901.2.1.1722024913.48.0.0; _uetsid=0400fa204b3911efbbe7c79b75a79f15; _uetvid=040115e04b3911efbf451b00643d02f2; _fbp=fb.1.1722024913585.561564863370991172; u_vp=980x964; AMP_c14fa5162b=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI0NDI1Y2RmMC05NGZmLTQ2OWEtOTY0Ni1kYzRiZDhlY2M4ODklMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzIyMDI0OTExNzgyJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcyMjAyNDkxMjM5NyUyQyUyMmxhc3RFdmVudElkJTIyJTNBNCUyQyUyMnBhZ2VDb3VudGVyJTIyJTNBMSU3RA==",  # noqa
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36",  # noqa
                    "X-Client-App": "web_mobile",
                },
            )

            if req.status == 200:
                with open(
                    "src/cs_services/js_data_items/csmoney.json", "w"
                ) as file:  # noqa
                    json.dump(await req.json(), file, indent=4)
                    return True

            return False

    async def get_all_data_by_itemname(
        self, item_name: str
    ) -> Union[dict[str, Union[str, int]], bool]:

        is_saved: bool = await self.save_data(item_name=item_name)

        if is_saved:

            with open(
                "src/cs_services/js_data_items/csmoney.json", "r"
            ) as file:  # noqa
                data_file: dict = json.load(file)

                data_to_response: dict = {
                    "count": len(data_file["items"]),
                    "items": [
                        {
                            "currency": "USD",
                            "rarity": item["pricing"],
                            "name": item["asset"]["names"]["short"],
                            "market_hash_name": item["asset"]["names"]["full"],
                            "quality": item["asset"]["quality"],
                            "stickers": item["stickers"],
                            "price": item["pricing"]["default"],
                        }
                        for item in data_file["items"]
                    ],
                }

                return data_to_response

        return False
