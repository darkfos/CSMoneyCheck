from typing import Annotated
from logging import Logger
from fastapi import APIRouter, Depends, status

from src.api.auth.auth_service import AuthService
from src.api.dto import NewsBase, NewsList
from src.api.services.news_service import NewsService
from src.enums_cs import APIRouterTagsEnum, APIRouterPrefixEnum  # noqa
from src.configs.logger_config import logger_dep, user_config
from src.api.dep import InterfaceUnitOfWork, UnitOfWork
from src.database.redis.redis_worker import RedisWorker
from src.api.dep import redis


news_router: APIRouter = APIRouter(
    prefix=APIRouterPrefixEnum.NEWS_PREFIX.value,
    tags=APIRouterTagsEnum.NEWS_TAGS.value,  # noqa
)


@news_router.post(
    path="/create",
    description="Создание новости - доступен для администратора",
    summary="Создание новости",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
async def create_review(
    logger: Annotated[Logger, Depends(logger_dep)],
    user_data: Annotated[dict, Depends(AuthService.verify_user)],
    uow: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    news: NewsBase,
) -> None:
    """
    NEWS ROUTER: Create new news
    """

    logger.info(msg="Create new news by admin", extra=user_config)

    await NewsService.create_news(token_data=user_data, uow=uow, news=news)  # noqa


@news_router.get(
    path="/all",
    description="Получение всех новостей",
    response_model=NewsList,
    summary="Все новости",
    status_code=status.HTTP_200_OK,
)
async def all_news(
    logger: Annotated[Logger, Depends(logger_dep)],
    uow: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    redis_db: Annotated[RedisWorker, Depends(redis)],
) -> NewsList:
    """
    News Router: Get all news
    :param logger:
    :param redis_db:
    """

    logger.info(msg="Get all news", extra=user_config)

    redis_data = await redis_db.get_value(key="news")
    if redis_data:
        return redis_data
    else:
        news = await NewsService.get_all_news(uow=uow)
        await redis_db.set_key(key="news", value=news.json())
        return news
