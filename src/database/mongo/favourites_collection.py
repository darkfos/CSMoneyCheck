from src.database.mongo.mongodb_worker import MongoDBWorker
from src.database.mongo.mongo_interfaces import (
    CreateInterface,
    GetOneInterface,
    GetAllInterface,
    DeleteInterface,  # noqa
)
from src.api.dto import CreateFavourite


class FavouritesCollection(
    MongoDBWorker,
    CreateInterface,
    GetOneInterface,
    GetAllInterface,
    DeleteInterface,  # noqa
):

    def __init__(self):
        super().__init__()
        self.fav_collection = self.db.get_collection("favourites")

    async def create(self, data: CreateFavourite) -> bool:
        req = await self.fav_collection.insert_one(document=data)
        if req:
            return True
        return False

    async def get_all(self):
        return await self.fav_collection.find()

    async def get_one(self, id_user: int):
        return await self.fav_collection.find_one(filter={"id_user": id_user})

    async def delete(self, id_fav: str):
        await self.fav_collection.delete_one(filter={"_id": id_fav})
