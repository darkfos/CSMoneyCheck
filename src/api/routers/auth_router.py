from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import Response  # noqa
from src.api.auth.auth_service import AuthService  # noqa
from src.api.dto.auth_dto import AuthUserData
from src.api.dep import InterfaceUnitOfWork, UnitOfWork
from src.api.services import UserService


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
    user_data: AuthUserData,
) -> None:
    """
    Endpoint - /register for create a new user
    :param credentials:
    :return:
    """

    return await UserService.create_new_user(user_data=user_data, uow=uow)
