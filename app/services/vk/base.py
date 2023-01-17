import logging

import vk_api

from apps.core.base import wait


class VKService:
    def __init__(self, login: str, password: str):
        session = vk_api.VkApi(login, password)
        session.auth()
        self.client = session.get_api()

    def send_to_wall(self):
        self.client.wall.post(message='Hello world!')

    @wait
    def get_account_counters(self, account_id: int):
        return self.client.account.getCounters(user_id=account_id)

    @wait
    def add_friend(self, account_id: int):
        try:
            self.client.friends.add(user_id=account_id)
            logging.info(f"Add request to add: [{account_id}]")
        except Exception as e:
            message = e.error.get('error_msg')

            if e.code == 177:
                return
            logging.error(f"Add failed: {message}")
            raise Exception(message)

    @wait
    def get_friends(self, account_id: int = None):
        if account_id:
            return self.client.friends.get(user_id=account_id)
        return self.client.friends.get()

    @wait
    def get_friends_count(self, account_id: int = None) -> int:
        if account_id:
            friends = self.client.friends.get(user_id=account_id)
        else:
            friends = self.client.friends.get()

        return friends.get('count', 0)

    @wait
    def get_account_info(self, account_id: int):
        return self.client.users.get(user_ids=account_id)
