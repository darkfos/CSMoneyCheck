from typing import List
from src.database.mongo.mongo_interfaces.create_interface import CreateInterface
from src.database.mongo.mongo_interfaces.get_all_interface import GetAllInterface
from src.database.mongo.mongo_interfaces.get_one_interface import GetOneInterface
from src.database.mongo.mongo_interfaces.delete_interface import DeleteInterface


__all__: List[str] = [
    "CreateInterface", "GetOneInterface",
    "GetAllInterface", "DeleteInterface"
]
