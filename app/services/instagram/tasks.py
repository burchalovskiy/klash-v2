import asyncio

from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI

from app.database.models import Account
from app.services.constants import SocialNetwork
from app.services.instagram.base import get_posts, get_stories, set_comment, set_cross_like
from app.utils.exceptions import BusinessLogicFault


def set_instagram_events(app: FastAPI) -> None:
    app.state.scheduler.add_job(
        task_save_instagram_post,
        CronTrigger.from_crontab("1 11 * * *"),
    )
    app.state.scheduler.add_job(
        task_save_instagram_stories,
        CronTrigger.from_crontab("2 12 * * *"),
    )
    app.state.scheduler.add_job(
        task_set_instagram_comment,
        CronTrigger.from_crontab("3 * * * *"),
    )
    app.state.scheduler.add_job(
        task_set_instagram_cross_like,
        CronTrigger.from_crontab("3 13 * * *"),
    )


async def task_save_instagram_post() -> None:
    tasks = []
    accounts = await Account.filter(is_enabled=True, type=SocialNetwork.INSTAGRAM.value)
    if not accounts:
        raise BusinessLogicFault('Accounts not found')

    for account in accounts:
        tasks.append(asyncio.create_task(get_posts(account)))
    await asyncio.gather(*tasks)


async def task_save_instagram_stories() -> None:
    tasks = []
    accounts = await Account.filter(is_enabled=True, type=SocialNetwork.INSTAGRAM.value)
    if not accounts:
        raise BusinessLogicFault('Accounts not found')

    for account in accounts:
        tasks.append(asyncio.create_task(get_stories(account)))
    await asyncio.gather(*tasks)


async def task_set_instagram_comment() -> None:
    tasks = [
        asyncio.create_task(set_comment()),
    ]
    await asyncio.gather(*tasks)


async def task_set_instagram_cross_like() -> None:
    tasks = [asyncio.create_task(set_cross_like())]
    await asyncio.gather(*tasks)
