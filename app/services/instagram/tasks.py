import asyncio
from loguru import logger

from app.database.models import Account
from app.services.constants import SocialNetwork
from app.services.instagram.base import get_posts, get_stories, set_comment
from app.utils.exceptions import BusinessLogicFault


async def task_save_instagram_post() -> None:
    tasks = []
    accounts = await Account.filter(is_enabled=True, type=SocialNetwork.INSTAGRAM.value)
    if not accounts:
        raise BusinessLogicFault('Accounts not found')

    for account in accounts:
        # tasks.append(asyncio.create_task(get_posts(account)))
        # tasks.append(asyncio.create_task(get_stories(account)))
        tasks.append(asyncio.create_task(set_comment()))
    await asyncio.gather(*tasks)


async def task_like_post() -> None:
    logger.info('Start update errors from Google Sheets')
    pass
