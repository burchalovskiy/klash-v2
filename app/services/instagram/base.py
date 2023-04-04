import os
import time
from datetime import datetime
from pathlib import Path
from random import randrange

import tortoise.exceptions
from instagrapi import Client as instagrapiClient
from instagrapi.exceptions import ClientForbiddenError

from app.core.config import get_app_settings
from app.database.models import Account, SocialAction, SocialActionLog, SocialPost, SocialPostURL, SocialUser
from app.services.constants import Action, ContentType
from app.utils.exceptions import BusinessLogicFault, ExceptionMessages

settings = get_app_settings()


class Limits:
    moment_likes: int = 50
    day_likes: int = 500
    moment_comments: int = 40
    day_comments: int = 200


async def log_in(login: str, password: str) -> instagrapiClient:
    dump_file = Path(f'{settings.media_path}/auth/{login}.json')

    cl = instagrapiClient()
    try:
        if dump_file.is_file():
            cl.load_settings(dump_file)
            cl.login(login, password)
            cl.get_timeline_feed()
        else:
            cl.login(login, password)
            open(dump_file, 'a').close()
            cl.dump_settings(dump_file)
    except ClientForbiddenError:
        os.remove(dump_file)

    return cl


async def get_posts(account: Account) -> None:
    client = await log_in(account.login, account.password)
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
            },
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
                    },
                )
        else:
            url = post.thumbnail_url if post.video_url is None else post.video_url
            content_type = ContentType.PHOTO.value if post.media_type == 1 else ContentType.VIDEO.value
            await SocialPostURL.get_or_create(
                url=url,
                defaults={
                    'post': social_post,
                    'content_type': content_type,
                },
            )


async def get_stories(account: Account) -> None:
    client = await log_in(account.login, account.password)
    user = client.user_info_by_username(account.login)
    stories = client.user_stories(int(user.pk))

    for story in stories:
        social_post, _ = await SocialPost.get_or_create(
            post_id=story.pk,
            defaults={
                'created_at': story.taken_at.isoformat(),
                'account': account,
                'post_url': f'https://www.instagram.com/stories/{account.login}/{story.pk}/',
            },
        )
        url = story.thumbnail_url if story.video_url is None else story.video_url
        await SocialPostURL.get_or_create(
            url=url,
            defaults={
                'post': social_post,
                'content_type': ContentType.STORIES.value,
            },
        )


async def set_comment() -> None:
    comment_count = 0
    actions = await SocialAction.filter(is_active=True, type=Action.COMMENT.name).prefetch_related()

    if not actions:
        raise tortoise.exceptions.DoesNotExist()

    for action in actions:
        users = await action.users
        if not users:
            raise tortoise.exceptions.DoesNotExist()

        for user in users:
            await _check_limits(action, user)
            account = await user.account
            client = await log_in(account.login, account.password)
            instagram_user = client.user_info_by_username(user.username)
            posts = client.user_medias(int(instagram_user.pk), 5)

            hashtags = action.values.get('hashtags')
            comments = action.values.get('comments')
            for post in posts:
                if not any(tag in post.caption_text for tag in hashtags):
                    continue

                _, created = await SocialActionLog.get_or_create(
                    message=f'https://www.instagram.com/p/{post.code}/',
                    defaults={
                        'user': user,
                        'action': action,
                    },
                )
                if not created:
                    continue

                for comment in comments:
                    if comment_count > Limits.moment_comments:
                        raise BusinessLogicFault(ExceptionMessages.LIMIT.value)
                    client.media_comment(post.id, comment)
                    time.sleep(randrange(3))


async def set_cross_like() -> None:
    like_count = 0
    actions = await SocialAction.filter(is_active=True, type=Action.CROSS_LIKE.name).prefetch_related()
    if not actions:
        raise tortoise.exceptions.DoesNotExist()

    for action in actions:
        users = await action.users
        if not users:
            raise tortoise.exceptions.DoesNotExist()

        for user in users:
            await _check_limits(action, user)

            account = await user.account
            client = await log_in(account.login, account.password)
            instagram_user = client.user_info_by_username(user.username)
            posts = client.user_medias(int(instagram_user.pk), 5)

            for post in posts:
                users_who_sent_likes = client.media_likers(post.pk)
                for user_like in users_who_sent_likes:
                    user_like_posts = client.user_medias(int(user_like.pk), 3)
                    for user_like_post in user_like_posts:
                        _, created = await SocialActionLog.get_or_create(
                            message=f'https://www.instagram.com/p/{user_like_post.code}/',
                            defaults={
                                'user': user,
                                'action': action,
                            },
                        )
                        if not created:
                            continue

                        if not post.has_liked:
                            if like_count > Limits.moment_likes:
                                raise BusinessLogicFault(ExceptionMessages.LIMIT.value)

                            client.media_like(post.id)
                            like_count += 1
                            time.sleep(30)


async def _check_limits(action: SocialAction, user: SocialUser) -> None:
    today = datetime.now()
    day_limit = await SocialActionLog.filter(
        action=action,
        user=user,
        send_at__year=today.year,
        send_at__month=today.month,
        send_at__day=today.day,
    ).count()
    if day_limit > Limits.day_comments:
        raise BusinessLogicFault(ExceptionMessages.LIMIT.value)
