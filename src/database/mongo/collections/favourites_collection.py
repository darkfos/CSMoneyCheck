from src.database.mongo.mongodb_worker import MongoDBWorker
from src.database.mongo.mongo_interfaces import (
    CreateInterface,
    GetOneInterface,
    GetAllInterface,
    DeleteInterface,  # noqa
)
from src.api.dto import CreateFavourite
from bson.objectid import ObjectId


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

    async def get_all(self, id_user):
        req = self.fav_collection.find({"id_user": int(id_user)})
        return await req.to_list(length=None)

    async def get_one(self, id_user: int):
        return await self.fav_collection.find_one({"id_user": id_user})

    async def delete(self, id_fav: str):
        req = await self.fav_collection.delete_one({"_id": ObjectId(id_fav)})
        return req
