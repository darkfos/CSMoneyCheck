from dotenv import load_dotenv
from os import getenv
from typing import Final


load_dotenv()


class DatabaseSettings:
    DB_URL: Final[str] = getenv("DB_URL")
    REDIS_HOST: Final[str] = getenv("REDIS_HOST")
    REDIS_PORT: Final[int] = int(getenv("REDIS_PORT"))
    REDIS_DB: Final[int] = int(getenv("REDIS_DB"))
    MONGODB: Final[str] = getenv("MONGODB_URL")
