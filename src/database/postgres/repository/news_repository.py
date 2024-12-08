from typing import List

from src.database.postgres.repository import GeneralRepository, GetOneInterface  # noqa
from asyncpg import Pool, Record
from src.database.postgres.models import News


class NewsRepository(GeneralRepository, GetOneInterface):  # noqa

    def __init__(self, pool: Pool):
        self.pool = pool
        self.model: News = News()
        super().__init__(model=self.model, session=pool)

    async def get_one(self, id_model: int) -> Record:
        """
        Get news by id
        :param id_model:
        :return:
        """

        async with self.pool.acquire() as ls:
            req = await ls.fetch("SELECT * FROM News WHERE id = $1", id_model)
            return req

    async def get_all(self) -> List[Record]:
        """
        Get all news by id
        :return:
        """

        async with self.pool.acquire() as ls:
            req = await ls.fetch("SELECT * FROM News")
            return req
