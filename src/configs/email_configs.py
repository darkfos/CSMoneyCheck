from typing import Final

from dotenv import load_dotenv
from os import getenv


load_dotenv()


class EmailConfig:
    EMAIL_URL: Final[str] = getenv("EMAIL_URL")
    EMAIL_PASSWORD: Final[str] = getenv("EMAIL_PASSWORD")
    EMAIL_HEADER: Final[str] = "Сообщение от CsMoney 📧"
