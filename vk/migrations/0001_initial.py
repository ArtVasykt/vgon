# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_password', models.CharField(max_length=70, verbose_name='Пароль')),
                ('user_login', models.CharField(max_length=70, verbose_name='Логин')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
