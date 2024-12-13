from src.enums_cs import ModelsEnum
from typing import LiteralString, Union
from asyncpg import Pool
from src.database.postgres.models import Users, UserType, News, Reviews  # noqa


class GeneralRepository:
    def __init__(
        self,
        model: Union[Users, UserType, News, Reviews],  # noqa
        session: Pool,
    ) -> None:
        self.model = model
        self.model_name: LiteralString[
            ModelsEnum.USER.value,
            ModelsEnum.USER_TYPE.value,
            ModelsEnum.FAVOURITE.value,
        ] = self.model.name
        self.session = session

    async def add_data(self, data: tuple) -> bool:
        """
        Добавление новой записи в модель
        :param data:
        :return:
        """

        async with self.session.acquire() as ls:
            try:
                stmt = await ls.execute(
                    f"INSERT INTO {self.model.name} ({", ".join(await self.model.columns())}) VALUES {await self.model.values_for_create()}",  # noqa
                    *data,
                )  # noqa
                if stmt:
                    return True
                raise Exception
            except Exception as ex:
                return False
