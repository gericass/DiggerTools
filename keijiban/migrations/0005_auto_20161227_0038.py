# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keijiban', '0004_tweet_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USERID', models.CharField(default='NOTHING', max_length=500, verbose_name='id')),
            ],
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='USERID',
        ),
    ]
