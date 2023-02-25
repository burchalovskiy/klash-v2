import uuid
from datetime import datetime

from fastapi_admin.models import AbstractAdmin
from tortoise import fields, models

from app.core.config import get_app_settings
from app.services.constants import SocialNetwork, ContentType, Action

settings = get_app_settings()


class BaseModel(models.Model):
    id = fields.BigIntField(pk=True)
    title = fields.CharField(max_length=256, description='Title', null=False)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)


class SocialPostURL(models.Model):
    id = fields.BigIntField(pk=True)
    post = fields.ForeignKeyField('models.SocialPost', 'urls')
    url = fields.CharField(max_length=800, default='', description='URL address of source')
    content_type = fields.CharEnumField(enum_type=ContentType)


class SocialPost(models.Model):
    id = fields.BigIntField(pk=True)
    post_id = fields.CharField(max_length=256, null=False)
    created_at = fields.DatetimeField(description='Created time')
    account = fields.ForeignKeyField('models.Account', 'account')
    caption = fields.CharField(max_length=2500, default='')
    post_url = fields.CharField(max_length=800, default='', description='URL address of post')

    urls: fields.ReverseRelation[SocialPostURL]

    def __str__(self):
        return f'{self.id}#{self.post_id}#'


class SocialUser(models.Model):
    id = fields.BigIntField(pk=True)
    account = fields.ForeignKeyField('models.Account')
    username = fields.CharField(max_length=256, null=False)
    actions: fields.ManyToManyRelation["SocialAction"] = fields.ManyToManyField(
        'models.SocialAction',
        related_name='users',
        through='user_actions',
    )

    def __str__(self):
        return self.username


class SocialAction(BaseModel):
    is_active = fields.BooleanField(default=True)
    type = fields.CharEnumField(enum_type=Action, null=False)
    values = fields.JSONField(max_length=16384, null=True)

    users: fields.ReverseRelation["SocialUser"]

    def __str__(self):
        return self.title


class SocialActionLog(models.Model):
    id = fields.BigIntField(pk=True)
    send_at = fields.DatetimeField(description='Created time', default=datetime.now())
    user = fields.ForeignKeyField('models.SocialUser')
    action = fields.ForeignKeyField('models.SocialAction')
    post_url = fields.CharField(max_length=800, default='', description='URL address of post')


class CrossPost(models.Model):
    id = fields.BigIntField(pk=True)
    post = fields.ForeignKeyField('models.SocialPost', 'post')
    is_send = fields.BooleanField(default=False, description='Post is send to new social network')
    send_date = fields.DatetimeField(description='Send time')

    def __str__(self):
        return f'{self.id}#{self.post}#'


class Channel(BaseModel):
    pass

    class Meta:
        abstract = True


class Account(BaseModel):
    type = fields.CharEnumField(enum_type=SocialNetwork)
    login = fields.CharField(
        max_length=256,
        default='',
        description='Phone or username for social network',
    )
    hashed_password = fields.CharField(max_length=256, default='', null=True)
    token = fields.CharField(max_length=256, default='', null=True)
    user = fields.ForeignKeyField('models.Admin', 'account')
    is_enabled = fields.BooleanField(default=True, description='Is enabled?')

    def __str__(self):
        return f'{self.login}#{self.type.value}'

    # async def save(self, *args, **kwargs) -> None:
    #     self.hashed_password = self.get_password_hash(self.hashed_password)
    #     await super().save(*args, **kwargs)

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return settings.pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return settings.pwd_context.hash(password)

    class PydanticMeta:
        exclude = ['hashed_password']


class Admin(AbstractAdmin):
    username = fields.CharField(max_length=256, default='', description='Username')
    last_login = fields.DatetimeField(description='Last login', default=datetime.now)

    def __str__(self):
        return f'{self.pk}#{self.username}'
