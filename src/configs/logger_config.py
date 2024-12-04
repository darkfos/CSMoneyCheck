import logging
from logging import Logger
from typing import Dict, Annotated


user_config: Dict[str, str] = {"user": "darkfos"}


async def logger_dep() -> Logger:
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        filename="logCS.log",
        level=logging.INFO,
        format="%(asctime)s %(user)-8s %(message)s"
    )
    return logger
