from fastapi import FastAPI
from src.api.routers.market_router import market_router
import uvicorn

app: FastAPI = FastAPI(
    title="API MarketService"
)

app.include_router(
    market_router
)


if __name__ == "__main__":
    uvicorn.run(app=app)