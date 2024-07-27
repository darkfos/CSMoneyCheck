from fastapi import FastAPI
from src.api.routers import api_v1_router
import uvicorn

app: FastAPI = FastAPI(
    title="API MarketService"
)

app.include_router(
    api_v1_router
)


if __name__ == "__main__":
    uvicorn.run(app=app)