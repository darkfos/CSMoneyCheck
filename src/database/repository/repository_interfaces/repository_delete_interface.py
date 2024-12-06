from abc import ABC, abstractmethod


class DeleteInterface(ABC):
    @abstractmethod
    async def delete_by_id(self, id_model: int) -> None:
        """
        Метод интерфейса для удаления по идентификатору
        :param id_model:
        :return:
        """

        raise NotImplementedError
