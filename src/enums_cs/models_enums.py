from enum import Enum
from typing import Final


class ModelsEnum(Enum):
    USER: Final[str] = "user"
    USER_TYPE: Final[str] = "usertype"
    FAVOURITE: Final[str] = "favourite"


class UserTypeEnum(Enum):
    USER: Final[int] = 1
    ADMIN: Final[int] = 2
