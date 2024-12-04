import asyncio

from fastapi import FastAPI
from src.api.routers import api_v1_router
import uvicorn


app: FastAPI = FastAPI(title="API MarketService")
app.include_router(api_v1_router)


async def start_application() -> None:
    uvicorn.run("main:app", reload=True)


if __name__ == "__main__":
    asyncio.run(start_application())