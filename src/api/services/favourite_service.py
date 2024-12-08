from src.database.mongo.favourites_collection import FavouritesCollection
from src.api.dto import CreateFavourite, FavouriteData
from src.api.exceptions import FavouriteException


class FavouriteService:

    @classmethod
    async def create_row_in_fav_collection(
        cls, data: FavouriteData, token_data: dict
    ) -> None:
        is_created: bool = await FavouritesCollection().create(
            data=CreateFavourite(
                id_user=token_data.get("sub"), items=data.model_dump()
            ).items
        )

        if not is_created:
            await FavouriteException.no_create_favourite()
