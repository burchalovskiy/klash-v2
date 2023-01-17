# from tortoise import models
#
# from app.database.models import Account
#
#
# class InstagramAccount(Account):
#     telegram_channel = models.ForeignKey(TelegramChannel, verbose_name='Канал Telegram',
#                                          on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.username
#
#
# class InstagramPost(models.Model):
#     CONTENT_TYPE = (
#         ('1', 'Фото'),
#         ('2', 'Видео'),
#     )
#     account = models.ForeignKey(InstagramAccount, verbose_name='Аккаунт Instagram', on_delete=models.CASCADE)
#     identifier = models.CharField(max_length=50, verbose_name='ID публикации в Instagram')
#     caption = models.CharField(max_length=2200, verbose_name='Описание публикации')
#     created_at = models.DateTimeField(verbose_name='Дата публикации')
#     content_type = models.CharField(max_length=1, choices=CONTENT_TYPE, blank=False, verbose_name="Тип публикации")
#     post_url = models.URLField(verbose_name='URL публикации в Instagram', max_length=800)
#     source_url = models.URLField(verbose_name='URL файла', max_length=800)
#     is_published = models.BooleanField(verbose_name='Опубликована в Telegram канале', default=False)
#
#     class Meta:
#         ordering = ["-created_at"]
#         verbose_name = "Публикация Instagram"
#         verbose_name_plural = "Публикации Instagram"
#
#     def __str__(self):
#         return self.identifier
