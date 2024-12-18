from asyncpg import Record
from typing import List
from src.api.dto import NewsBase, NewsList
from src.enums_cs.models_enums import UserTypeEnum
from src.api.dep import InterfaceUnitOfWork
from src.api.exceptions import UserException


class NewsService:

    @classmethod
    async def create_news(
        cls, token_data: dict, uow: InterfaceUnitOfWork, news: NewsBase
    ) -> None:
        """
        NewsService: Create news, access for admin
        """

        async with uow:
            user_data: Record = await uow.user_repository.get_one(
                id_model=int(token_data.get("sub"))
            )
            if int(user_data.get("id_user_type")) == UserTypeEnum.ADMIN.value:
                await uow.news_repository.add_data(
                    (news.news_version, news.news_text, news.news_tag)
                )  # noqa
                return
            await UserException.no_auth_user()

    @classmethod
    async def get_all_news(cls, uow: InterfaceUnitOfWork) -> NewsList:
        """
        NewsService: Get all news
        """

        async with uow:
            news_data: List[Record] = await uow.news_repository.get_all()
            print(news_data)
            all_news: NewsList = NewsList(news=[])
            for news in news_data:
                all_news.news.append(
                    NewsBase(
                        news_version=news.get("news_version"),
                        news_text=news.get("news_text"),
                        news_tag=news.get("news_tag"),
                    )
                )
            return all_news
