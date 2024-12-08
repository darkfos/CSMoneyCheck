from typing import Annotated, Any, Dict

from pydantic import BaseModel, Field


class FavouriteData(BaseModel):
    items: Annotated[Dict[Any, Any], Field()]


class CreateFavourite(FavouriteData):
    id_user: Annotated[int, Field(gt=0)]
