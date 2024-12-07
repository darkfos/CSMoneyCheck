import json

from redis.asyncio import Redis
from typing import Any
from src.configs import DatabaseSettings


class RedisWorker:

    redis = Redis(
        host=DatabaseSettings.REDIS_HOST,
        port=DatabaseSettings.REDIS_PORT,
        db=DatabaseSettings.REDIS_DB,
    )

    @classmethod
    async def set_key(cls, key, value) -> None:
        """
        Set data in redis DB
        :param key:
        :param value:
        :return:
        """

        await cls.redis.set(name=key, value=value, ex=60)

    @classmethod
    async def get_value(cls, key) -> Any:
        """
        Get data from redis DB by key
        :param key:
        :return:
        """

        data = await cls.redis.get(name=key)
        if data:
            return json.loads(data.decode("utf-8"))
        else:
            return False
