from dotenv import load_dotenv
from os import getenv
from typing import Final


load_dotenv()


class DatabaseSettings:
    DB_URL: Final[str] = getenv("DB_URL")
