import datetime
from typing import Final, Any
from src.enums_cs import ModelsEnum, UserTypeEnum
from src.database.models import ModelInterface


class Users(ModelInterface):

    def __init__(
        self,
        email: str,
        hashed_password: str,
        username: str,
        date_reg: datetime.date,
        id_user_type: int = None,
    ) -> None:
        self.__name: Final[str] = ModelsEnum.USER.value
        self.__id_user_type: int = (
            id_user_type if id_user_type else UserTypeEnum.USER.value
        )
        self.__email = email
        self.__hashed_password = hashed_password
        self.__username = username
        self.__date_reg = date_reg

    async def create_model_script(self) -> str:
        return """
        CREATE TABLE users IF NOT EXISTS (
        id SERIAL PRIMARY KEY,
        id_user_type INT,
        email TEXT,
        hashed_password TEXT,
        username VARCHAR(155),
        date_reg DATE,
        FOREIGN KEY (id_user_type) REFERENCES usertype (id)
        )
        """

    async def columns(self) -> tuple[str]:
        return (
            "id_user_type",
            "email",
            "hashed_password",
            "username",
            "date_reg",
        )  # noqa

    async def values(self) -> tuple[Any]:
        return (
            self.__id_user_type,
            self.__email,
            self.__hashed_password,
            self.__username,
            self.__date_reg,
        )
