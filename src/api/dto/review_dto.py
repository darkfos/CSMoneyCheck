from pydantic import BaseModel, Field
from typing import Annotated, List, Union


class CreateReview(BaseModel):
    text_review: Annotated[str, Field()]


class ReviewList(BaseModel):
    reviews: Annotated[List[Union[List, CreateReview]], Field()]
