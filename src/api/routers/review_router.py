from logging import Logger

from fastapi import APIRouter, Depends, status
from src.api.dep import InterfaceUnitOfWork, UnitOfWork
from src.api.services import ReviewService
from src.api.auth.auth_service import AuthService
from src.configs import logger_dep, user_config  # noqa
from src.enums_cs import APIRouterTagsEnum, APIRouterPrefixEnum
from src.api.dto import CreateReview, ReviewList  # noqa
from src.api.dep import redis
from src.database.redis.redis_worker import RedisWorker
from typing import Annotated


review_router: APIRouter = APIRouter(
    prefix=APIRouterPrefixEnum.REVIEWS_PREFIX.value,
    tags=APIRouterTagsEnum.REVIEWS_TAGS.value,
)


@review_router.post(
    path="/add",
    description="""
    Создание отзыва от лица пользователя
    """,
    summary="Создание отзыва",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
async def add_review(
    logger: Annotated[Logger, Depends(logger_dep)],
    user_data: Annotated[dict, Depends(AuthService.verify_user)],
    uow: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    new_review: CreateReview,
) -> None:
    """
    Получение всех отзывов
    :logger:
    :user_data:
    :uow:
    :new_review:
    """

    logger.info(msg="Create review by user", extra=user_config)

    await ReviewService.create_review(
        token_data=user_data, uow=uow, new_review=new_review
    )


@review_router.get(
    path="/all",
    description="""Получение всех отзывов""",
    response_model=ReviewList,
    status_code=status.HTTP_200_OK,
    summary="Все отзывы",
)
async def all_reviews(
    uow: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    redis_db: Annotated[RedisWorker, Depends(redis)],
    logger: Annotated[Logger, Depends(logger_dep)],
) -> ReviewList:
    """
    REVIEW ROUTER: Get all reviews
    :param uow:
    :param logger:
    """

    logger.info(msg="Get all reviews by user", extra=user_config)

    redis_data = await redis_db.get_value(key="reviews")
    if redis_data:
        return redis_data
    else:
        news = await ReviewService.get_all(uow=uow)
        await redis_db.set_key(key="reviews", value=news.json())
        return news
