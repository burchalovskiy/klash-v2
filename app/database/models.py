import uuid
from datetime import datetime

from fastapi_admin.models import AbstractAdmin
from tortoise import fields, models


class Admin(AbstractAdmin):
    email = fields.CharField(max_length=200, default='', description='E-mail')
    last_login = fields.DatetimeField(description='Последний вход', default=datetime.now)
    created_at = fields.DatetimeField(auto_now_add=True, description='Дата создания')

    def __str__(self):
        return f'{self.pk}#{self.username}'


class BaseModel(models.Model):
    id = fields.UUIDField(pk=True, editable=False, default=uuid.uuid4)
    created_at = fields.DatetimeField(auto_now_add=True, description='Дата создания')
    title = fields.CharField(max_length=256, description='Наименованиe')

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)


class Post(BaseModel):
    pass


class Channel(BaseModel):
    pass


class Account(BaseModel):
    username = fields.CharField(max_length=256)
