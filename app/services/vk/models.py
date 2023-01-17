# import csv
# import datetime
# import io
# import os
#
# from django.core.validators import FileExtensionValidator
# from django.db import models
# from django.utils.deconstruct import deconstructible
# from encrypted_model_fields.fields import EncryptedCharField
#
# from apps.core.base import ModelEnum
# from apps.vk.services.base import VKService
#
#
# @deconstructible
# class UploadPath(object):
#     def __init__(self, folder_name: str) -> None:
#         self._folder_name = folder_name
#
#     def __call__(self, instance, filename):
#         return os.path.join(self._folder_name, filename)
#
#
# class VKAccount(models.Model):
#     title = models.CharField('Наименование', max_length=64)
#     username = models.CharField('Логин', max_length=100, unique=True)
#     token = EncryptedCharField('Токен', max_length=100)
#     friends_file = models.FileField('Файл со списком друзей',
#                                     upload_to=UploadPath('vk_friends'),
#                                     validators=[FileExtensionValidator(['csv'])],
#                                     null=True, blank=True,
#                                     help_text='Файл должен содержать список "id" пользователей VK')
#
#     def save(self, *args, **kwargs):
#         super(VKAccount, self).save(*args, **kwargs)
#         if getattr(self, 'friends_file', True):
#             self._file_to_model()
#
#     def _file_to_model(self):
#         file = self.friends_file.read().decode('utf-8')
#         reader = list(csv.DictReader(io.StringIO(file), delimiter=";"))
#
#         friends_count = VKService(login=self.username, password=self.token).get_friends_count()
#         objs = [
#             VKFriendsStatistics(
#                 vk_account=self,
#                 sent_date=datetime.datetime.today(),
#                 status=VKFriendsStatistics.Status.EMPTY.name,
#                 total_friends_count=friends_count,
#                 friend_id=e.get('id')
#             )
#             for e in reader
#         ]
#         VKFriendsStatistics.objects.filter(vk_account=self).delete()
#         msg = VKFriendsStatistics.objects.bulk_create(objs)
#
#     def __str__(self) -> str:
#         return self.title
#
#     class Meta(object):
#         verbose_name = 'Аккаунт ВКонтакте'
#         verbose_name_plural = 'Аккаунты ВКонтакте'
#
#
# class VKFriendsStatistics(models.Model):
#     class Status(ModelEnum):
#         ACCEPT = 'Принята'
#         SEND = 'Отправлена'
#         EMPTY = 'Не отправлена'
#
#     vk_account = models.ForeignKey(VKAccount, on_delete=models.CASCADE, verbose_name='Аккаунт')
#     sent_date = models.DateField('Дата отправки заявки')
#     status = models.CharField('Статус', choices=Status.choices(), max_length=64)
#     total_friends_count = models.IntegerField('Общее количество друзей')
#     friend_id = models.IntegerField('ID добавляемого пользователя')
#
#     class Meta(object):
#         verbose_name = 'Статистика друзей ВКонтакте'
#         verbose_name_plural = 'Статистика друзей ВКонтакте'
