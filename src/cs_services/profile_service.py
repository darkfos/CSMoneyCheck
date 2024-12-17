from aiohttp import ClientSession
from src.configs import OtherSettings
from typing import Union


class ProfileService:

    @classmethod
    async def get_inventory_data(cls, profile_id: int) -> Union[dict, None]:
        """
        Get profile items data

        :param profile_id:
        """

        async with ClientSession(OtherSettings.STEAMWEBAPI_URL) as session:
            req = await session.get(
                url="inventory",
                params={
                    "key": OtherSettings.STEAMWEBAPI_TOKEN,
                    "steam_id": profile_id,
                },  # noqa
            )

            if req.status == 200:
                return await req.json()
            return None

    @classmethod
    async def get_item_data(cls, market_hash_name: str) -> Union[dict, None]:
        """
        Get item data by hash_name

        :param market_hash_name:
        """

        async with ClientSession(OtherSettings.STEAMWEBAPI_URL) as session:
            req = await session.get(
                url="item",
                params={
                    "key": OtherSettings.STEAMWEBAPI_TOKEN,
                    "market_hash_name": market_hash_name,
                },
            )

            if req.status == 200:
                return await req.json()
            return None
