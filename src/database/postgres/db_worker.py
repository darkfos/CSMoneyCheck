import asyncpg
from asyncpg import Pool
from src.configs import DatabaseSettings


class DBWorker:
    async def __aenter__(self):
        self.pool: Pool = await asyncpg.create_pool(DatabaseSettings.DB_URL)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.pool.close()
