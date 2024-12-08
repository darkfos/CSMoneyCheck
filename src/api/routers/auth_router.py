from logging import Logger
from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import Response  # noqa
from src.api.auth.auth_service import AuthService  # noqa
from src.api.dto import AuthModel
from src.api.dto.auth_dto import AuthUserData
from src.api.dep import InterfaceUnitOfWork, UnitOfWork
from src.api.services import UserService
from src.configs.logger_config import logger_dep

auth_router: APIRouter = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post(
    path="/register",
    response_model=None,
    description="""
    Create a new user
    """,
    summary="Create user",
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    uow: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],  # noqa
    logger: Annotated[Logger, Depends(logger_dep)],
    user_data: AuthUserData,
) -> None:
    """
    Endpoint - /register for create a new user
    :param credentials:
    :return:
    """

    logger.info(msg=f"Auth: Регистрация пользователя email={user_data.email}")  # noqa
    return await UserService.create_new_user(user_data=user_data, uow=uow)


@auth_router.post(
    path="/login",
    description="""
    Authentication user
    """,
    summary="Auth user",
    status_code=status.HTTP_200_OK,
    response_model=None,
)
async def login_user(
    uow: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    logger: Annotated[Logger, Depends(logger_dep)],
    user_data: AuthUserData,
    response: Response,
) -> None:
    logger.info(msg=f"Auth: авторизация пользователя email={user_data.email}")  # noqa
    token_data: AuthModel = await UserService.login_user(
        user_data=user_data, uow=uow
    )  # npqa
    response.set_cookie(
        key="access_token",
        value=token_data.access_token,  # noqa
    )
    response.set_cookie(
        key="refresh_token",
        value=token_data.refresh_token,  # noqa
    )
