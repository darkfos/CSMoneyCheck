from abc import ABC, abstractmethod


class GetAllInterface(ABC):

    @abstractmethod
    async def get_all(self):
        """
        Getting all data frm mongo collection
        :return:
        """

        raise NotImplementedError
