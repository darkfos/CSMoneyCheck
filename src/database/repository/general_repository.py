from src.enums_cs import ModelsEnum
from typing import LiteralString, Union
from asyncpg import Pool
from src.database.models import Users, UserType


class GeneralRepository:
    def __init__(
        self,
        model: Union[Users, UserType],
        pool: Pool,
    ) -> None:
        self.model = model
        self.model_name: LiteralString[
            ModelsEnum.USER.value,
            ModelsEnum.USER_TYPE.value,
            ModelsEnum.FAVOURITE.value,
        ] = self.model.name
        self.session = pool

    async def add_data(self, data: tuple) -> bool:
        """
        Добавление новой записи в модель
        :param data:
        :return:
        """

        async with self.session.acquire() as local_session:
            try:
                stmt = await local_session.execute(
                    f"INSERT INTO {self.model.name} {self.model.get_columns()} VALUES {self.model.get_values()}",  # noqa
                    *data,
                )  # noqa
                if stmt:
                    return True
                raise Exception
            except Exception:
                return False
