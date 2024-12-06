import asyncpg
from asyncpg import Pool
from src.configs import DatabaseSettings


class DBWorker:
    def __aenter__(self):
        self.pool: Pool = asyncpg.create_pool(DatabaseSettings.DB_URL)
        yield self

    def __aexit__(self, exc_type, exc_val, exc_tb):
        self.pool.close()
