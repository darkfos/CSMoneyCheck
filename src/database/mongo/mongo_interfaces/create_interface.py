from abc import ABC, abstractmethod


class CreateInterface(ABC):

    @abstractmethod
    async def create(self, data):
        """
        Create new row in mongo collection
        :return:
        """

        raise NotImplementedError
