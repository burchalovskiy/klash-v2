from typing import Any, Awaitable, List, Optional, Union

from redis import Redis
from redis.asyncio import from_url

from app.core.config import get_app_settings


class RedisCache:
    def __init__(self):
        self.redis_cache: Optional[Redis] = None

    async def init_cache(self):
        settings = get_app_settings()
        self.redis_cache = await from_url(settings.redis_url)

    async def keys(self, pattern: Any) -> Union[List[Any], Any]:
        return await self.redis_cache.keys(pattern)  # type: ignore[misc, union-attr]

    async def set_json(self, key: str, value: dict) -> None:
        return await self.redis_cache.json().set(key, '$', value)  # type: ignore[union-attr]

    async def get_json(self, key: str) -> Any:
        return await self.redis_cache.json().get(key, '$')  # type: ignore[union-attr]

    async def set(self, key: str, value: str) -> bool | None:
        return await self.redis_cache.set(key, value)  # type: ignore[misc, union-attr]

    async def get(self, key: str) -> Any:
        return await self.redis_cache.get(key)  # type: ignore[misc, union-attr]

    async def close(self) -> None:
        await self.redis_cache.flushdb()  # type: ignore[misc, union-attr]
        await self.redis_cache.close()  # type: ignore[misc, union-attr]


redis_cache = RedisCache()
