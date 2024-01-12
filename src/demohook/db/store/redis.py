
from typing import Optional

import redis.asyncio as redis
from conf.settings import settings

rds = None

def get_redis() -> Optional[redis.Redis]:
    global rds
    if rds is None and settings.redis_host and settings.redis_port:
        rds = redis.from_url( # type: ignore
            f"redis://{settings.redis_host}:{settings.redis_port}",
            encoding="utf-8",
            decode_responses=True,
        )
        return rds
    else:
        return None

async def set_key(key: str, value: str) -> None:
    rds = get_redis()
    if rds:
        await rds.set(key, value)

async def get_key(key: str) -> Optional[str]:
    rds = get_redis()
    if rds:
        return await rds.get(key)
    else:
        return None

