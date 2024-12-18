from pydantic import BaseModel, Field
from typing import Annotated, List


class NewsBase(BaseModel):
    news_version: Annotated[str, Field(max_length=50)]
    news_text: Annotated[str, Field()]
    news_tag: Annotated[str, Field(max_length=75)]


class NewsList(BaseModel):
    news: Annotated[List[NewsBase], Field()]
