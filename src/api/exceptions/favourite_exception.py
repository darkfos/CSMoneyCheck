from fastapi.exceptions import HTTPException
from fastapi import status


class FavouriteException:

    @classmethod
    async def no_create_favourite(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Не удалось создать запись в избранном",
        )
