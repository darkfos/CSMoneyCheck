from fastapi.exceptions import HTTPException
from fastapi import status


class ReviewExcp:
    @classmethod
    async def no_create_review(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не удалось создать отзыв"
        )
