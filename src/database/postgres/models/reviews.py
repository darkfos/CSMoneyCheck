from typing import Any, Final
from src.database.postgres.models import ModelInterface


class Reviews(ModelInterface):

    def __init__(self, id_user: int = None, text_review: str = None):
        self.__name: Final[str] = "reviews"
        self.id_user = id_user
        self.text_review = text_review

    @property
    def name(self) -> str:
        return self.__name

    @staticmethod
    async def create_model_script() -> str:
        return """
        CREATE TABLE IF NOT EXISTS reviews (
        id SERIAL PRIMARY KEY,
        id_user INT,
        text_review TEXT,
        FOREIGN KEY (id_user) REFERENCES users (id)
        );
        """

    @staticmethod
    async def values_for_create() -> str:
        return "($1, $2)"

    async def columns(self) -> tuple[str]:
        return ("id_user", "text_review")

    async def values(self) -> tuple[Any]:
        return (
            self.id_user,
            self.text_review,
        )
