from dotenv import load_dotenv
from os import getenv
from typing import Final


load_dotenv()


class AuthSettings:
    JWT_SECRET_KEY: Final[str] = getenv("JWT_SECRET_KEY")
    JWT_REFRESH_SECRET_KEY: Final[str] = getenv("JWT_REFRESH_SECRET_KEY")
