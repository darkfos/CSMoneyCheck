from src.api.routers.csmoney_router import cs_money_router
from src.api.routers.market_router import market_router
from src.api.routers.auth_router import auth_router
from src.api.routers.favourites_router import fav_router
from src.enums_cs import APIRouterTagsEnum, APIRouterPrefixEnum
from fastapi import APIRouter


api_v1_router: APIRouter = APIRouter(
    prefix=APIRouterPrefixEnum.API_V1_PREFIX.value,
    tags=APIRouterTagsEnum.API_V1_TAGS.value,
)

api_v1_router.include_router(auth_router)
api_v1_router.include_router(market_router)
api_v1_router.include_router(cs_money_router)
api_v1_router.include_router(fav_router)
