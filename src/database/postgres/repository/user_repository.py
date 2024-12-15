from typing import List

from src.database.postgres.models import Users
from src.database.postgres.repository import (
    GeneralRepository,
    GetAllInterface,
    GetOneInterface,
    UpdateInterface,
    DeleteInterface,
)
from asyncpg import Record
from asyncpg import Pool


class UserRepository(
    GeneralRepository,
    GetOneInterface,
    GetAllInterface,
    UpdateInterface,
    DeleteInterface,
):
    def __init__(self, session: Pool):
        self.model = Users()
        self.session = session
        super().__init__(model=self.model, session=self.session)

    async def update_data(self, id_model: int, data_to_update: dict) -> bool:
        """
        Method repository for update data in user table
        :param id_model:
        :param data_to_update:
        :return:
        """

        async with self.session.acquire() as ls:
            for data in data_to_update.items():
                await ls.execute(
                    f"UPDATE {self.model.name} SET {data[0]} = $1 WHERE id = $2",  # noqa
                    *(data[1], id_model),
                )
            return True

    async def update_user_secret_key(self, id_model: int, key: str) -> None:
        """
        Update user secret key
        :param id_model:
        :param key:
        """

        async with self.session.acquire() as ls:
            req = await ls.execute(
                f"UPDATE {self.model.name} SET secret_key = $1 WHERE id = $2",
                *(key, id_model),
            )  # noqa
            return req

    async def get_all_by_id(self, id_model: int) -> List[Record]:
        """
        Method repository for get all record from user table
        :param id_model:
        :return:
        """

        async with self.session.acquire() as ls:
            req = ls.fetch(
                f"SELECT * FROM {self.model.name} WHERE id = ?", *(id_model,)
            )
            return req

    async def get_one(self, id_model: int) -> Record:
        """
        Method repository for get one record from user table
        :param id_model:
        :return:
        """

        async with self.session.acquire() as ls:
            req = await ls.fetchrow(
                f"SELECT * FROM {self.model.name} WHERE id = $1", *(id_model,)
            )
            return req

    async def delete_by_id(self, id_model: int) -> None:
        """
        Method repository for delete record from user table
        :param id_model:
        :return:
        """

        async with self.session.acquire() as ls:
            req = await ls.execute(
                f"DELETE FROM {self.model.name} WHERE id = $1", *(id_model,)
            )  # noqa
            return req

    async def find_by_email(self, email: str) -> Record:
        """
        Method reposifory for find user by email
        :param email:
        :return:
        """

        async with self.session.acquire() as ls:
            req = await ls.fetch(
                f"SELECT * FROM {self.model.name} WHERE email = $1", email
            )
            return req

    async def find_by_secret(self, secret: str) -> Record:
        """
        Поиск пользователя по секретному ключу
        :param secret:
        """

        async with self.session.acquire() as ls:
            req = await ls.fetch(
                f"SELECT * FROM {self.model.name} WHERE secret_key = $1", secret  # noqa
            )
            return req
