import uvicorn
from fastapi import FastAPI
from src.api.routers import api_v1_router
from src.database import DBWorker
from src.database.postgres.models import Users, UserType, Reviews, News  # noqa
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = DBWorker()
    await db.create_connection()
    async with db.pool.acquire() as connect:
        await connect.execute(
            await UserType.create_model_script()
        )  # Create usertype table
        await connect.execute(await UserType.create_user_types())
        await connect.execute(await Users.create_model_script())  # noqa
        await connect.execute(await Reviews.create_model_script())  # noqa
        await connect.execute(await News.create_model_script())  # noqa

    yield


app: FastAPI = FastAPI(title="API CSMoney", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_v1_router)


def run_app() -> None:
    # Start project

    uvicorn.run(app=app, host="127.0.0.1", port=8000)
