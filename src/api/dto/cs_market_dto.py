from pydantic import BaseModel
from typing import List, Dict, Union


class MarketItemsData(BaseModel):

    count: int
    items: List[Dict[Union[str, int, float], Union[str, int, list, float]]]