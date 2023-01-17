import uuid
from datetime import datetime

from fastapi_admin.models import AbstractAdmin
from tortoise import fields, models


class Admin(AbstractAdmin):
    email = fields.CharField(max_length=200, default='')
    last_login = fields.DatetimeField(description='Last Login', default=datetime.now)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk}#{self.username}'


class BaseModel(models.Model):
    id = fields.UUIDField(pk=True, editable=False, default=uuid.uuid4)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)


class User(BaseModel):
    phone_number = fields.CharField(max_length=15, unique=True)
    balance = fields.IntField(default=0)

