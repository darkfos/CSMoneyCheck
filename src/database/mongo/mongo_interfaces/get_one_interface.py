from abc import ABC, abstractmethod


class GetOneInterface(ABC):

    @abstractmethod
    async def get_one(self, *args):
        """
        Get one row from mongo collection
        :return:
        """

        raise NotImplementedError
