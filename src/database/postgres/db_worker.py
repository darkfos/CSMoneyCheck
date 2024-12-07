from asyncpg import create_pool, Pool
from src.configs import DatabaseSettings


class DBWorker:

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance

    async def create_connection(self):
        self.pool: Pool = await create_pool(DatabaseSettings.DB_URL)
