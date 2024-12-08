from src.api.routers.csmoney_router import cs_money_router
from src.api.routers.market_router import market_router
from src.api.routers.auth_router import auth_router
from src.api.routers.favourites_router import fav_router
from fastapi import APIRouter


api_v1_router: APIRouter = APIRouter(prefix="/api/v1", tags=["API_V1"])

api_v1_router.include_router(auth_router)
api_v1_router.include_router(market_router)
api_v1_router.include_router(cs_money_router)
api_v1_router.include_router(fav_router)
