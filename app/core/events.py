from typing import Callable

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI
from fastapi_admin.providers.login import UsernamePasswordProvider
from loguru import logger
from redis.asyncio import from_url

from app.admin import admin_app
from app.core.settings.app import AppSettings
from app.database.models import Admin
from app.database.settings import init_db


def create_start_app_handler(
        app: FastAPI,
        settings: AppSettings,
) -> Callable:
    async def start_app() -> None:
        await init_db(app)
        await connect_redis(app, settings)
        await init_admin(app)
        await start_scheduler(app)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    @logger.catch
    async def stop_app() -> None:
        await disconnect_redis(app)
        await stop_scheduler(app)

    return stop_app


async def connect_redis(app: FastAPI, settings: AppSettings) -> None:
    logger.info('Connecting to Redis')
    app.state.redis = from_url(settings.redis_url)


async def disconnect_redis(app: FastAPI) -> None:
    logger.info('Closing connection to Redis')
    await app.state.redis.close()


async def start_scheduler(app: FastAPI) -> None:
    logger.info('Start Scheduler')
    redis_config = app.state.redis.connection_pool.connection_kwargs
    redis_job_store = RedisJobStore(
        host=redis_config.get('host', 'localhost'),
        port=redis_config.get('port', '6379'),
    )

    app.state.scheduler = BackgroundScheduler()
    app.state.scheduler.configure(
        jobstores={'default': redis_job_store},
        executors={
            'default': ThreadPoolExecutor(),
        },
        job_defaults={'coalesce': True, 'max_instance': 1},
    )
    # app.state.scheduler.add_job(
    #     # update_company_errors,
    #     # CronTrigger.from_crontab("* * * * *"),
    # )

    app.state.scheduler.start()


async def stop_scheduler(app: FastAPI) -> None:
    logger.info('Stop Scheduler')
    app.state.scheduler.shutdown()


async def init_admin(app: FastAPI) -> None:
    await admin_app.configure(
        providers=[UsernamePasswordProvider(admin_model=Admin)],
        redis=app.state.redis,
    )
