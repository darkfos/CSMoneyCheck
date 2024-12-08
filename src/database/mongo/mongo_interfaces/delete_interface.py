from abc import ABC, abstractmethod


class DeleteInterface:

    @abstractmethod
    async def delete(self, *args):
        """
        Delete row from mongo collection
        :return:
        """

        raise NotImplementedError
