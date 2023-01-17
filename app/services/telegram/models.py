#
#
# def validate_telegram_channel(value):
#     if value.startswith('@'):
#         return value
#     else:
#         raise ValidationError("Необходимо вписывать название Telegram канала в формате @telegramchannel")
#
#
# class TelegramChannel(models.Model):
#     name = models.CharField(max_length=250, verbose_name='Логин Telegram канала', blank=False,
#                             validators=[validate_telegram_channel])
#
#     class Meta:
#         verbose_name = "Telegram канал"
#         verbose_name_plural = "Telegram каналы"
#
#     def __str__(self):
#         return self.name
#
#
# class TelegramPost(models.Model):
#     post_id = models.CharField(max_length=250, verbose_name='ID публикации', blank=False)
#     channel = models.ForeignKey(TelegramChannel, verbose_name='Канал Telegram', on_delete=models.CASCADE)
#     posted_at = models.DateTimeField(verbose_name='Дата публикации', blank=False)
#     likes_count = models.IntegerField(verbose_name='Количество лайков', default=0)
#     views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)
#
#     @property
#     def telegram_post_url(self):
#         channel_name = TelegramChannel.objects.get(pk=self.channel).name
#         return f'https://t.me/{channel_name}/{self.post_id}'
#
#     class Meta:
#         ordering = ["-posted_at"]
#         verbose_name = "Публикация Telegram"
#         verbose_name_plural = "Публикации Telegram"
#
#     def __str__(self):
#         return self.post_id
#
#
# class TelegramUser(models.Model):
#     user_id = models.CharField(max_length=250, verbose_name='Telegram User ID', blank=False)
#     username = models.CharField(max_length=250, verbose_name='Telegram логин', blank=False)
#     phone_number = PhoneField(verbose_name='Номер телефона ', blank=False)
#     api_id = models.CharField(max_length=16, verbose_name='Telegram API ID', blank=False)
#     api_hash = models.CharField(max_length=64, verbose_name='Telegram API Hash', blank=False)
#
#     class Meta:
#         verbose_name = "Пользователь Telegram"
#         verbose_name_plural = "Пользователи Telegram"
#
#     def __str__(self):
#         return self.username
