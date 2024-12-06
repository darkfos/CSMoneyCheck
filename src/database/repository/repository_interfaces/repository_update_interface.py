from abc import ABC, abstractmethod


class UpdateInterface(ABC):
    @abstractmethod
    async def update_data(self, id_model: int, data_to_update) -> bool:
        """
        Метод интерфейса для обновления данных
        :param id_model:
        :param data_to_update:
        :return:
        """

        raise NotImplementedError
