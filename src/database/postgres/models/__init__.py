from src.database.postgres.models.models_interfaces.model_interface import (
    ModelInterface,
)  # noqa
from src.database.postgres.models.user_model import Users
from src.database.postgres.models.user_type_model import UserType
from src.database.postgres.models.news import News
from src.database.postgres.models.reviews import Reviews
from typing import List


__all__: List[str] = ["ModelInterface", "Users", "UserType", "Reviews", "News"]  # noqa
