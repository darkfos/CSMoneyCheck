import datetime
from typing import Final, Any
from src.enums_cs import ModelsEnum, UserTypeEnum
from src.database.postgres.models import ModelInterface


class Users(ModelInterface):

    def __init__(
        self,
        email: str = None,
        hashed_password: str = None,
        username: str = None,
        date_reg: datetime.date = None,
        secret_key: str = None,
        id_user_type: int = None,
    ) -> None:
        self.__name: Final[str] = ModelsEnum.USER.value
        self.__id_user_type: int = (
            id_user_type if id_user_type else UserTypeEnum.USER.value
        )
        self.__email = email
        self.__hashed_password = hashed_password
        self.__username = username
        self.__secret_key = secret_key
        self.__date_reg = date_reg

    @staticmethod
    async def create_model_script() -> str:
        return """
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        id_user_type INT,
        email TEXT UNIQUE,
        hashed_password BYTEA,
        username VARCHAR(155),
        secret_key TEXT,
        date_reg DATE,
        FOREIGN KEY (id_user_type) REFERENCES usertype (id)
        )
        """

    @staticmethod
    async def values_for_create() -> str:
        return "($1, $2, $3, $4, $5, $6)"

    async def columns(self) -> tuple[str]:
        return (
            "id_user_type",
            "email",
            "hashed_password",
            "username",
            "secret_key",
            "date_reg",
        )  # noqa

    async def values(self) -> tuple[Any]:
        return (
            self.__id_user_type,
            self.__email,
            self.__hashed_password,
            self.__username,
            self.__secret_key,
            self.__date_reg,
        )

    @property
    def name(self) -> str:
        return self.__name
