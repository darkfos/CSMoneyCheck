from dotenv import load_dotenv
from os import getenv
from typing import Final


load_dotenv()


class AuthSettings:
    JWT_SECRET_KEY: Final[str] = getenv("JWT_SECRET_KEY")
    JWT_REFRESH_SECRET_KEY: Final[str] = getenv("JWT_REFRESH_SECRET_KEY")
    JWT_SECRET_LIVE: Final[int] = int(getenv("JWT_SECRET_LIVE"))
    JWT_REFRESH_LIVE: Final[int] = int(getenv("JWT_REFRESH_LIVE"))
    JWT_ALGORITHM: Final[str] = getenv("JWT_ALGORITHM")

    # ADMIN DATA
    ADMIN_EMAIL: Final[str] = getenv("ADMIN_EMAIL")
    ADMIN_PASSWORD: Final[str] = getenv("ADMIN_PASSWORD")
    