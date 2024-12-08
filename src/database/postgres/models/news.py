from src.database.postgres.models import ModelInterface
from typing import Final, Any


class News(ModelInterface):

    def __init__(
        self,
        news_version: str = None,
        news_text: str = None,
        news_tag: str = None,  # noqa
    ) -> None:
        self.news_version = news_version
        self.news_text = news_text
        self.news_tag = news_tag
        self.__name: Final[str] = "news"

    @staticmethod
    async def create_model_script() -> str:
        return """
        CREATE TABLE IF NOT EXISTS news (
        id SERIAL PRIMARY KEY,
        news_version VARCHAR(50),
        news_text TEXT,
        news_tag VARCHAR(75)
        );
        """

    @staticmethod
    async def values_for_create() -> str:
        return "($1, $2, $3)"

    @property
    def name(self) -> str:
        return self.__name

    async def columns(self) -> tuple[str]:
        return ("news_version", "news_text", "news_tag")

    async def values(self) -> tuple[Any]:
        return (self.news_version, self.news_text, self.news_tag)
