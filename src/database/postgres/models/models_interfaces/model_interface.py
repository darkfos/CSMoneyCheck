from abc import ABC, abstractmethod
from typing import Any


class ModelInterface(ABC):

    @abstractmethod
    async def columns(self) -> tuple[str]:
        raise NotImplementedError

    @abstractmethod
    async def values(self) -> tuple[Any]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def create_model_script() -> str:
        raise NotImplementedError
