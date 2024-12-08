from motor.motor_asyncio import AsyncIOMotorClient
from src.configs import DatabaseSettings


class MongoDBWorker:
    def __init__(self):
        self.engine_client: AsyncIOMotorClient = AsyncIOMotorClient(
            DatabaseSettings.MONGODB,
            **{"zlibCompressionLevel": 7, "compressors": "zlib"}
        )
        self.db = self.engine_client.get_database("csmoney")
