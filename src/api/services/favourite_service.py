from src.database.mongo.collections.favourites_collection import (
    FavouritesCollection,
)  # noqa
from src.api.dto import CreateFavourite, FavouriteData
from src.api.exceptions import FavouriteException


class FavouriteService:

    @classmethod
    async def create_row_in_fav_collection(
        cls, data: FavouriteData, token_data: dict
    ) -> None:
        is_created: bool = await FavouritesCollection().create(
            data=CreateFavourite(
                id_user=token_data.get("sub"), items=data.items
            ).model_dump()
        )

        if not is_created:
            await FavouriteException.no_create_favourite()

    @classmethod
    async def get_my_favourites(cls, token_data: dict):
        user_fav_data = await FavouritesCollection().get_all(
            id_user=token_data.get("sub")
        )
        if user_fav_data:
            for data in user_fav_data:
                data["_id"] = str(data.get("_id"))
            return user_fav_data
        await FavouriteException.no_found_favourites()

    @classmethod
    async def delete_fav(cls, token_data: dict, id_fav: str) -> None:
        is_deleted = await FavouritesCollection().delete(id_fav=id_fav)
        if is_deleted:
            return
        await FavouriteException.no_delete_favourite()
