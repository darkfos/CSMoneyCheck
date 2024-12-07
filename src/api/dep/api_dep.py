from src.database import RedisWorker


async def redis() -> RedisWorker:
    return RedisWorker()
