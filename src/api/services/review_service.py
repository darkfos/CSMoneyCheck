from src.api.dto import CreateReview
from src.api.dep import UnitOfWork
from typing import Dict, Union
from datetime import datetime
from src.api.exceptions import ReviewExcp


class ReviewService:
    @classmethod
    async def create_review(
            cls,
            new_review: CreateReview,
            uow: UnitOfWork,
            token_data: Dict[Union[str, int], Union[int, str, datetime.date]]
    ) -> None:
        """
        Review Service: Создание отзыва
        :new_review:
        :uow:
        :token_data:
        """

        async with uow:
            is_created = await uow.review_repository.add_data(
                data=(int(token_data.get("sub")), new_review.text_review)
            )
            if is_created:
                return

            await ReviewExcp.no_create_review()
