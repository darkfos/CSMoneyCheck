from src.database.models import ModelInterface
from src.enums_cs.models_enums import ModelsEnum
from typing import Final, Any


class UserType(ModelInterface):

    def __init__(self, name_type=None) -> None:
        self.__name_type: Final[str] = name_type
        self.__name = ModelsEnum.USER_TYPE.value

    async def columns(self) -> tuple[str]:
        return ("name_type",)

    async def values(self) -> tuple[Any]:
        return (self.__name_type,)

    @property
    def name(self) -> str:
        return self.__name
