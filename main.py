from fastapi import FastAPI
from src.api.routers import api_v1_router
from src.api.routers.page_router import page_router
from fastapi.staticfiles import StaticFiles
import uvicorn


if __name__ == "__main__":
    app: FastAPI = FastAPI(title="API MarketService")
    app.mount("/static", StaticFiles(directory="src/static"), name="static")
    app.include_router(api_v1_router)
    app.include_router(page_router)
    uvicorn.run(app=app)
