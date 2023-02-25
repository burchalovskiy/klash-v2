import logging
import time
from pathlib import Path

import asyncio
from random import randrange

import tortoise.exceptions
from instagrapi import Client as instagrapiClient
from tortoise.query_utils import Prefetch

from app.database.models import Account, SocialPost, SocialPostURL, SocialUser, SocialAction, SocialActionLog
from app.services.constants import ContentType, Action
from app.utils.exceptions import ClientFault, ExceptionMessages


async def log_in(login: str, password: str) -> instagrapiClient:
    cl = instagrapiClient()
    cl.login(login, password)

    return cl


async def get_posts(account: Account) -> None:
    client = await log_in(account.login, account.hashed_password)
    user = client.user_info_by_username(account.login)
    posts = client.user_medias(int(user.pk), 5)

    for post in posts:
        social_post, _ = await SocialPost.get_or_create(
            post_id=post.pk,
            defaults={
                'created_at': post.taken_at.isoformat(),
                'account': account,
                'caption': post.caption_text,
                'post_url': f'https://www.instagram.com/p/{post.code}/',
            }
        )

        if post.media_type == 8:
            for res in post.resources:
                url = res.thumbnail_url if res.video_url is None else res.video_url
                content_type = ContentType.PHOTO.value if res.media_type == 1 else ContentType.VIDEO.value
                await SocialPostURL.get_or_create(
                    url=url,
                    defaults={
                        'post': social_post,
                        'content_type': content_type,
                    }
                )
        else:
            url = post.thumbnail_url if post.video_url is None else post.video_url
            content_type = ContentType.PHOTO.value if post.media_type == 1 else ContentType.VIDEO.value
            await SocialPostURL.get_or_create(
                url=url,
                defaults={
                    'post': social_post,
                    'content_type': content_type,
                }
            )

    client.logout()


async def get_stories(account: Account) -> None:
    client = await log_in(account.login, account.hashed_password)
    user = client.user_info_by_username(account.login)
    stories = client.user_stories(int(user.pk))

    for story in stories:
        social_post, _ = await SocialPost.get_or_create(
            post_id=story.pk,
            defaults={
                'created_at': story.taken_at.isoformat(),
                'account': account,
                'post_url': f'https://www.instagram.com/stories/{account.login}/{story.pk}/',
            }
        )
        url = story.thumbnail_url if story.video_url is None else story.video_url
        await SocialPostURL.get_or_create(
            url=url,
            defaults={
                'post': social_post,
                'content_type': ContentType.STORIES.value,
            }
        )

    client.logout()


async def set_comment() -> None:
    actions = await SocialAction.filter(
        is_active=True, type=Action.COMMENT.name
    ).prefetch_related(
        Prefetch("users", queryset=SocialUser.all().prefetch_related(
            Prefetch("account", queryset=Account.all())
        )),
    )

    if not actions:
        raise tortoise.exceptions.DoesNotExist()

    for action in actions:
        users = await action.users
        if not users:
            raise tortoise.exceptions.DoesNotExist()

        for user in users:
            account = await user.account
            client = await log_in(account.login, account.hashed_password)
            instagram_user = client.user_info_by_username(user.username)
            posts = client.user_medias(int(instagram_user.pk), 5)

            hashtags = action.values.get('hashtags')
            comments = action.values.get('comments')
            for post in posts:
                if not any(tag in post.caption_text for tag in hashtags):
                    continue

                _, created = await SocialActionLog.get_or_create(
                    post_url=f'https://www.instagram.com/p/{post.code}/',
                    defaults={
                        'user': user,
                        'action': action,
                    }
                )
                if not created:
                    continue

                if action.values.get('send_like'):
                    client.media_like(post.id)

                for comment in comments:
                    client.media_comment(post.id, comment)
                    time.sleep(randrange(3))

            client.logout()
