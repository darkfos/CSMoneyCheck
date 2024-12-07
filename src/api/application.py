import uvicorn
from fastapi import FastAPI
from src.api.routers import api_v1_router
from src.database import DBWorker
from src.database.postgres.models import Users, UserType  # noqa
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with DBWorker() as connect:
        await connect.pool.execute(
            await UserType.create_model_script()
        )  # Create usertype table
        await connect.pool.execute(await UserType.create_user_types())
        await connect.pool.execute(
            await Users.create_model_script()
        )  # Create user table
    yield


app: FastAPI = FastAPI(title="API CSMoney", lifespan=lifespan)
app.include_router(api_v1_router)


def run_app() -> None:
    # Start project

    uvicorn.run(app=app, host="127.0.0.1", port=8000)
