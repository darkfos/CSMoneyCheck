from typing import List

from src.database.postgres.repository import (
    GetAllInterface,
    GetOneInterface,
    GeneralRepository,
)  # noqa
from src.database.postgres.models import Users
from asyncpg import Pool, Record


class UserTypeRepository(GeneralRepository, GetAllInterface, GetOneInterface):
    def __init__(self, pool) -> None:
        self.model: Users = Users()
        self.pool: Pool = pool
        super().__init__(model=self.model, pool=self.pool)

    async def get_one(self, id_model: int) -> Record:
        """
        Method for get one record from usertype table
        :param id_model:
        :return:
        """

        async with self.pool.acquire() as session:
            req = session.fetchone(
                f"SELECT * FROM {self.model.name} WHERE id = ?", (id_model,)
            )
            return req

    async def get_all_by_id(self, id_model: int) -> List[Record]:
        """
        Method for get all records from usertype table
        :param id_model:
        :return:
        """

        async with self.pool.acquire() as session:
            req = session.fetchall(
                f"SELECT * FROM {self.model.name} WHERE id = ?", (id_model,)
            )
            return req
