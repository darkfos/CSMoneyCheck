from src.database.postgres.models import ModelInterface
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

    @staticmethod
    async def create_model_script() -> str:
        return """
        CREATE TABLE IF NOT EXISTS usertype (
        id SERIAL PRIMARY KEY,
        name_type VARCHAR(60) UNIQUE
        )
        """

    @staticmethod
    async def create_user_types() -> str:
        return """
        INSERT INTO usertype (id, name_type) VALUES
        (1, 'user'),
        (2, 'admin')
        ON CONFLICT (name_type) DO NOTHING;
        """

    @staticmethod
    async def values_for_create() -> str:
        return "(?, ?)"
