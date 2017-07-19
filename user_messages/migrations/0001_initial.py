# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 08:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created at')),
                ('delivered_at', models.DateTimeField(blank=True, null=True, verbose_name='delivered at')),
                ('level', models.IntegerField(verbose_name='level')),
                ('message', models.TextField(verbose_name='message')),
                ('extra_tags', models.TextField(blank=True, verbose_name='extra tags')),
                ('_metadata', models.TextField(blank=True, verbose_name='meta data')),
                ('deliver_once', models.BooleanField(default=True, verbose_name='deliver once')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
    ]
