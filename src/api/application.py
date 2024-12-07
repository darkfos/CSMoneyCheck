import uvicorn
from fastapi import FastAPI
from src.api.routers import api_v1_router


app: FastAPI = FastAPI(title="API CSMoney")
app.include_router(api_v1_router)


def run_app() -> None:
    # Start project

    uvicorn.run(app=app, host="127.0.0.1", port=8000)
