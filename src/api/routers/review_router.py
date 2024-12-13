from logging import Logger

from fastapi import APIRouter, Depends, status
from src.api.dep import InterfaceUnitOfWork, UnitOfWork
from src.api.services import ReviewService
from src.api.auth.auth_service import AuthService
from src.configs import logger_dep, user_config
from src.enums_cs import APIRouterTagsEnum, APIRouterPrefixEnum
from src.api.dto import CreateReview
from typing import Annotated


review_router: APIRouter = APIRouter(
    prefix=APIRouterPrefixEnum.REVIEWS_PREFIX.value,
    tags=APIRouterTagsEnum.REVIEWS_TAGS.value
)


@review_router.post(
    path="/add",
    description="""
    Создание отзыва от лица пользователя
    """,
    summary="Создание отзыва",
    response_model=None,
    status_code=status.HTTP_201_CREATED
)
async def add_review(
        logger: Annotated[Logger, Depends(logger_dep)],
        user_data: Annotated[dict, Depends(AuthService.verify_user)],
        uow: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
        new_review: CreateReview
) -> None:
    """
    Получение всех отзывов
    :logger:
    :user_data:
    :uow:
    :new_review:
    """

    await ReviewService.create_review(token_data=user_data, uow=uow, new_review=new_review)