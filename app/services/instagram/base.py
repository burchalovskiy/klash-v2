import logging
from typing import List

from instagrapi import Client as instagrapiClient

from app.database.models import Account


async def log_in(login: str, password: str) -> instagrapiClient:
    try:
        cl = instagrapiClient()
        # cl.set_proxy(os.getenv('PROXY'))
        cl.login(login, password)
    except Exception as e:
        logging.error(e)
    else:
        return cl


async def get_posts(account: Account) -> None:
    client = await log_in(account.login, account.hashed_password)
    user = client.user_info_by_username(account.login)
    account_existed_posts = list(InstagramPost.objects.filter(account=account).values_list('identifier', flat=True))
    new_account_posts: List[InstagramPost] = list()
    available_post = list()

    end_cursor = None
    while end_cursor != '':
        try:
            available_post, end_cursor = cl.user_medias_paginated(int(instagram_user.pk), 30, end_cursor=end_cursor)
        except Exception as e:
            logging.error(e)
        finally:
            cl.logout()

        for post in available_post:
            if post.pk in account_existed_posts:
                continue

            if post.resources:
                for item in post.resources:
                    new_account_posts.append(InstagramPost(
                        account=account,
                        identifier=post.pk,
                        caption=post.caption_text,
                        created_at=post.taken_at.isoformat(),
                        post_url=f'https://www.instagram.com/p/{post.code}/',
                        content_type=str(item.media_type),
                        source_url=item.thumbnail_url if item.video_url is None else item.video_url
                    ))
            else:
                new_account_posts.append(InstagramPost(
                    account=account,
                    identifier=post.pk,
                    caption=post.caption_text,
                    created_at=post.taken_at.isoformat(),
                    post_url=f'https://www.instagram.com/p/{post.code}/',
                    content_type=str(post.media_type),
                    source_url=post.thumbnail_url if post.video_url is None else post.video_url
                ))

    InstagramPost.objects.bulk_create(new_account_posts)
    logging.info(f"Add {len(new_account_posts)} new posts to instagram: {account.username}")
