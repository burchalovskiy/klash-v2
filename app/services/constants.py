from enum import Enum


class SocialNetwork(Enum):
    INSTAGRAM = 'Instagram'
    VK = 'VK'
    TELEGRAM = 'Telegram'


class ContentType(Enum):
    PHOTO = 'Photo'
    VIDEO = 'Video'
    STORIES = 'Stories'


class Action(Enum):
    LIKE = 'LIKE'
    CROSS_LIKE = 'CROSS_LIKE'
    COMMENT = 'COMMENT'
