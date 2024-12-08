from typing import List
from src.database.postgres.repository.repository_interfaces.repository_delete_interface import (  # noqa
    DeleteInterface,
)
from src.database.postgres.repository.repository_interfaces.repository_update_interface import (  # noqa
    UpdateInterface,
)  # noqa
from src.database.postgres.repository.repository_interfaces.repository_get_all_interface import (  # noqa
    GetAllInterface,
)  # noqa
from src.database.postgres.repository.repository_interfaces.repository_get_one_interface import (  # noqa
    GetOneInterface,
)  # noqa
from src.database.postgres.repository.general_repository import (
    GeneralRepository,
)  # noqa
from src.database.postgres.repository.user_repository import UserRepository  # noqa
from src.database.postgres.repository.user_type_repository import (
    UserTypeRepository,
)  # noqa


__all__: List[str] = [
    "DeleteInterface",
    "UpdateInterface",
    "GetOneInterface",
    "GetAllInterface",
    "GeneralRepository",
    "UserTypeRepository",
    "UserRepository",
]
