from fastapi import HTTPException, status


class MarketException:

    @staticmethod
    async def not_found_a_items():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Не удалось найти предметы!"
        )