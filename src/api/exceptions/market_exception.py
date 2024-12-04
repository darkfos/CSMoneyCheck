from fastapi import HTTPException, status
from src.api.exceptions.enum_for_excp import ServiceErrors


class MarketException:

    @staticmethod
    async def not_found_a_items(txt_for_detail: ServiceErrors):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=txt_for_detail
        )
