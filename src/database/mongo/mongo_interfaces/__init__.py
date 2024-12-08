from typing import List
from src.database.mongo.mongo_interfaces.create_interface import CreateInterface  # noqa
from src.database.mongo.mongo_interfaces.get_all_interface import (
    GetAllInterface,
)  # noqa
from src.database.mongo.mongo_interfaces.get_one_interface import (
    GetOneInterface,
)  # noqa
from src.database.mongo.mongo_interfaces.delete_interface import DeleteInterface  # noqa


__all__: List[str] = [
    "CreateInterface",
    "GetOneInterface",
    "GetAllInterface",
    "DeleteInterface",
]
