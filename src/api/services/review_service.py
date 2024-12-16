from src.api.dto import CreateReview, ReviewList
from src.api.dep import UnitOfWork, InterfaceUnitOfWork
from typing import Dict, Union
from datetime import datetime
from src.api.exceptions import ReviewExcp


class ReviewService:
    @classmethod
    async def create_review(
        cls,
        new_review: CreateReview,
        uow: UnitOfWork,
        token_data: Dict[Union[str, int], Union[int, str, datetime.date]],
    ) -> None:
        """
        Review Service: Create review
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

    @classmethod
    async def get_all(cls, uow: InterfaceUnitOfWork) -> ReviewList:  # noqa
        """
        Review Service: Get all reviews
        """

        async with uow:
            reviews = await uow.review_repository.get_all_reviews()
            all_reviews_list: ReviewList = ReviewList(reviews=[])
            for review in reviews:
                all_reviews_list.reviews.append(CreateReview(text_review=review[-1])) # noqa
            return all_reviews_list
