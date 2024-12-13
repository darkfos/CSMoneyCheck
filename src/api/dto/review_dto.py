from pydantic import BaseModel, Field
from typing import Annotated


class CreateReview(BaseModel):
    text_review: Annotated[str, Field()]
