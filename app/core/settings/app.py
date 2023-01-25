import logging
import sys
from typing import Any, Dict, List, Tuple

from loguru import logger
from pydantic import SecretStr

from app.core.logging import InterceptHandler
from app.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    debug: bool = False
    docs_url: str = '/docs'
    title: str = 'Klash'
    version: str = '2.0.0'
    api_prefix: str = "/api"
    jwt_token_prefix: str = 'Token'
    allowed_hosts: List[str] = ['*']
    logging_level: int = logging.INFO
    loggers: Tuple[str, str] = ('uvicorn.asgi', 'uvicorn.access')

    # env
    redis_url: str
    secret_key: SecretStr
    vcs_ref: str
    release: str
    token: str

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            'debug': self.debug,
            'docs_url': self.docs_url,
            'title': self.title,
            'version': self.version,
        }

    def configure_logging(self) -> None:
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in self.loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(level=self.logging_level)]

        logger.configure(handlers=[{'sink': sys.stderr, 'level': self.logging_level}])
