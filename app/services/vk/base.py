import json
import logging

import tortoise
import vk_api
from vk_api.vk_api import VkApiMethod

from app.database.models import Account, SocialAction, SocialActionLog, SocialPost, SocialUser
from app.services.constants import Action


async def log_in(login: str, password: str) -> VkApiMethod:
    session = vk_api.VkApi(login, password)
    session.auth()
    return session.get_api()


async def _check_limits(action: SocialAction, user: SocialUser) -> None:
    pass
    # today = datetime.now()
    # day_limit = await SocialActionLog.filter(
    #     action=action,
    #     user=user,
    #     send_at__year=today.year,
    #     send_at__month=today.month,
    #     send_at__day=today.day,
    # ).count()
    # if day_limit > Limits.day_comments:
    #     raise BusinessLogicFault(ExceptionMessages.LIMIT.value)


async def add_friend():
    friends_ids = []
    friends_count = 50
    #  TODO Сохранение списка друзей. Брать срезами по 50

    actions = await SocialAction.filter(is_active=True, type=Action.ADD_USERS.name).prefetch_related()

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
            user_friends_count = client.friends.get().get('count', 0)

            for user_id in friends_ids:
                friend_log = {
                    'friend_id': user_id,
                    'friends_count': user_friends_count,
                }

                try:
                    client.friends.add(user_id=user_id)
                except Exception as e:
                    friend_log.update(
                        {
                            'success': False,
                        }
                    )
                    message = e.error.get('error_msg')
                    if e.code == 177:
                        return

                    raise Exception(message)
                else:
                    friend_log.update(
                        {
                            'success': True,
                        }
                    )
                finally:
                    await SocialActionLog.create(message=json.dumps(friend_log), user=user, action=action)


async def set_stories(account: Account) -> None:
    client = await log_in(account.login, account.password)

    stories = []

    for story in stories:
        client.stories.getPhotoUploadServer()
        client.stories.getVideoUploadServer()
        # TODO https://vk.com/dev/stories.getVideoUploadServer=
