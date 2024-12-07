from abc import ABC, abstractmethod
from asyncpg import Record


class GetOneInterface(ABC):
    @abstractmethod
    async def get_one(self, id_model: int) -> Record:
        """
        Метод интерфейса для получения 1 записи по идентификатору
        :param id_model:
        :return:
        """

        raise NotImplementedError
