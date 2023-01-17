import datetime
import logging
import os
import random
from time import sleep
from typing import List

import telebot

from telebot import types

from apps.instagram.models import InstagramPost
from apps.telegram.models import TelegramChannel, TelegramPost


def sendTelegramPosts(posts: List[InstagramPost]):
    telegramPosts = []
    try:
        bot = telebot.TeleBot(random.choice(os.getenv('TELEGRAM_BOT_TOKEN').split(' ')))
        caption = posts[0].caption
        post_url = posts[0].post_url
        media = []
        for post in posts:
            channel = TelegramChannel.objects.get(name=post.account.telegram_channel)

            logging.info(f"Update Telegram {channel}")
            media_type = types.InputMediaPhoto if post.content_type == '1' else types.InputMediaVideo

            if post_url == post.post_url and len(posts) > 1:
                media.append(media_type(media=post.source_url))
                continue
            else:
                media.append(media_type(media=post.source_url))

            media[0].caption = f'{caption}\n\nСсылка:\n{post_url}'

            telegram_message = bot.send_media_group(chat_id=channel.name, media=media)
            telegramPosts.append(TelegramPost(
                telegram_post_id=telegram_message[0].message_id,
                telegram_channel=channel,
                telegram_posted_at=datetime.datetime.fromtimestamp(telegram_message[0].date, tz=datetime.timezone.utc)))

            # sleep few second Telegram bot api: Error code 429 Too many requests
            sleep(len(media))
            InstagramPost.objects.filter(post_url=post_url).update(is_published=True)

            media = [media_type(media=post.source_url)]
            post_url = post.post_url
            caption = post.caption

        bot.close()

    except Exception as e:
        logging.error(e)

    finally:
        TelegramPost.objects.bulk_create(telegramPosts)