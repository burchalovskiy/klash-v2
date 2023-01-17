import datetime
import io
from csv import DictReader
from logging import Logger

from apps.vk.models import VKAccount, VKFriendsStatistics
from apps.vk.services.base import VKService

logger = Logger(__name__)


class VKFriends:
    def __init__(self):
        self.add_users_count = 50

    def add(self):
        for account in VKAccount.objects.all():
            client = VKService(account.username, account.token)
            friends_count = client.get_friends_count()
            friends = VKFriendsStatistics.objects.filter(
                vk_account=account,
                status=VKFriendsStatistics.Status.EMPTY.name
            ).all()[:self.add_users_count]

            for friend in friends:
                client.add_friend(friend.friend_id)

                VKFriendsStatistics.objects.update_or_create(
                    vk_account=account,
                    sent_date=datetime.date.today(),
                    status=VKFriendsStatistics.Status.SEND.name,
                    total_friends_count=friends_count,
                    friend_id=friend.friend_id
                )
