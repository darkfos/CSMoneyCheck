from fastapi import APIRouter, Depends, status
from fastapi.responses import Response
from src.api.auth.auth_service import AuthService
from src.api.dto.auth_dto import AuthUserData


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
async def register_user(user_data: AuthUserData) -> None:
    """
    Endpoint - /register for create a new user
    :param credentials:
    :return:
    """

    ...
