from src.enums_cs import ModelsEnum
from typing import LiteralString
from asyncpg import Pool


class GeneralRepository:
    def __init__(
            self,
            model: LiteralString[
                ModelsEnum.USER.value,
                ModelsEnum.USER_TYPE.value,
                ModelsEnum.FAVOURITE.value
            ],
            pool: Pool
    ) -> None:
        self.model = model
        self.session = pool

    async def _add_data(self, data: tuple) -> bool:
        """
        Добавление новой записи в модель
        :param data:
        :return:
        """

        async with self.session.acquire() as local_session:
            try:
                stmt = await local_session.execute(f"""
                INSERT INTO {self.model.name} {self.model.get_columns()} VALUES {self.model.get_values()}
                """, *data)
                if stmt:
                    return True
                raise Exception
            except Exception:
                return False
