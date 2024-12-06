from abc import ABC, abstractmethod
from asyncpg import Record
from typing import List


class GetAllInterface(ABC):
    @abstractmethod
    async def get_all_by_id(self, id_model: int) -> List[Record]:
        """
        Метод сервиса для получение всех записей по идентификатору
        :param id_model:
        :return:
        """
        
        raise NotImplementedError
