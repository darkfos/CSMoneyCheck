from typing import List

from src.database.postgres.models import Users
from src.database.postgres.repository import (
    GeneralRepository,
    GetAllInterface,
    GetOneInterface,
    UpdateInterface,
    DeleteInterface,
)
from asyncpg import Pool, Record


class UserRepository(
    GeneralRepository,
    GetOneInterface,
    GetAllInterface,
    UpdateInterface,
    DeleteInterface,
):
    def __init__(self, pool: Pool):
        self.model = Users()
        self.pool = pool
        super().__init__(model=self.model, pool=self.pool)

    async def update_data(self, id_model: int, data_to_update) -> bool:
        """
        Method repository for update data in user table
        :param id_model:
        :param data_to_update:
        :return:
        """

        pass

    async def get_all_by_id(self, id_model: int) -> List[Record]:
        """
        Method repository for get all record from user table
        :param id_model:
        :return:
        """

        async with self.pool.acquire() as session:
            req = session.fetchall(
                f"SELECT * FROM {self.model.name} WHERE id = ?", *(id_model,)
            )
            return req

    async def get_one(self, id_model: int) -> Record:
        """
        Method repository for get one record from user table
        :param id_model:
        :return:
        """

        async with self.pool.acquire() as session:
            req = session.fetchone(
                f"SELECT * FROM {self.model.name} WHERE id = ?", *(id_model,)
            )
            return req

    async def delete_by_id(self, id_model: int) -> None:
        """
        Method repository for delete record from user table
        :param id_model:
        :return:
        """

        async with self.pool.acquire() as session:
            req = session.execute(
                f"DELETE FROM {self.model.name} WHERE id = ?", *(id_model,)
            )  # noqa
            return req
