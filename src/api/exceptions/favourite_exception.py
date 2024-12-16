from fastapi.exceptions import HTTPException
from fastapi import status


class FavouriteException:

    @classmethod
    async def no_create_favourite(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="No to create user favourite",
        )

    @classmethod
    async def no_found_favourites(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No found user favourites",  # noqa
        )

    @classmethod
    async def no_delete_favourite(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No to delete favourite",  # noqa
        )
