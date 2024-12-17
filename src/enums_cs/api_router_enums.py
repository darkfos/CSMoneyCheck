from enum import Enum
from typing import Final, List


class APIRouterPrefixEnum(Enum):
    """
    Prefix for APIRouter's
    """

    MARKET_PREFIX: Final[str] = "/market"
    CSMONEY_PREFIX: Final[str] = "/csmoney"
    USER_PREFIX: Final[str] = "/user"
    USER_TYPE_PREFIX: Final[str] = "/ust"
    FAVOURITE_PREFIX: Final[str] = "/favourite"
    NEWS_PREFIX: Final[str] = "/news"
    REVIEWS_PREFIX: Final[str] = "/reviews"
    AUTH_PREFIX: Final[str] = "/auth"
    API_V1_PREFIX: Final[str] = "/api/v1"
    PROFILE_PREFIX: Final[str] = '/profile'


class APIRouterTagsEnum(Enum):
    """
    Tags for APIRouter's
    """

    MARKET_TAGS: List[str] = ["Market"]
    CSMONEY_TAGS: List[str] = ["CsMoney"]
    USER_TAGS: List[str] = ["User"]
    USER_TYPE_TAGS: List[str] = ["UserType"]
    FAVOURITE_TAGS: List[str] = ["Favourite"]
    NEWS_TAGS: List[str] = ["News"]
    REVIEWS_TAGS: List[str] = ["Reviews"]
    AUTH_TAGS: List[str] = ["Auth"]
    API_V1_TAGS: List[str] = ["API-V1"]
    PROFILE_TAGS: List[str] = ["Profile"]
