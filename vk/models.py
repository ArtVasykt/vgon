from django.db import models
from django.utils import timezone


class User(models.Model):
    user_password = models.CharField(max_length=70, verbose_name='пароль')
    user_login = models.CharField(max_length=70, verbose_name='логин')
    pub_date = models.DateTimeField(verbose_name='дата', default=timezone.now)

    def __str__(self):
        return self.user_login

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
