from abc import ABC, abstractmethod
from typing import Type
from src.database.postgres.repository import UserRepository, UserTypeRepository  # noqa


class InterfaceUnitOfWork(ABC):

    user_repository: Type[UserRepository]
    user_type_repository: Type[UserTypeRepository]

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError
