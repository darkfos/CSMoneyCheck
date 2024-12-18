from dotenv import load_dotenv
from os import getenv
from typing import Final


load_dotenv()


class OtherSettings:

    STEAMWEBAPI_URL: Final[str] = getenv("STEAMWEBAPI_URL")
    STEAMWEBAPI_TOKEN: Final[str] = getenv("STEAMWEBAPI_TOKEN")
