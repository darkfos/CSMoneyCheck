from fastapi.exceptions import HTTPException
from fastapi import status


class NewsExceptions:
    @classmethod
    async def no_create_news(cls):
        await HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No create news"
        )
