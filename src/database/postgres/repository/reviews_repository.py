from typing import List

from src.database.postgres.models import Reviews
from src.database.postgres.repository import (
    GeneralRepository,
    GetOneInterface,
    GetAllInterface,
)
from asyncpg import Pool, Record


class ReviewsRepository(GeneralRepository, GetOneInterface, GetAllInterface):  # noqa
    def __init__(self, session: Pool) -> None:
        self.pool = session
        self.model = Reviews()
        super().__init__(model=self.model, session=self.pool)

    async def get_one(self, id_model: int) -> Record:
        """
        Get reviews by id
        :param id_model:
        :return:
        """

        async with self.pool.acquire() as ls:
            req = await ls.fetch(
                "SELECT * FROM reviews WHERE id = $1", id_model
            )  # noqa
            return req

    async def get_all_by_id(self, id_model: int) -> List[Record]:
        """
        Get all reviews by id_user
        :param id_model:
        :return:
        """

        async with self.pool.acquire() as ls:
            req = await ls.fetch(
                "SELECT * FROM reviews WHERE id_user = $1", id_model
            )  # noqa
            return req
