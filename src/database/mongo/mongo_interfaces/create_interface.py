from abc import ABC, abstractmethod


class CreateInterface:

    @abstractmethod
    async def create(self, data):
        """
        Create new row in mongo collection
        :return:
        """

        raise NotImplementedError
