# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-24 10:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='order', to=settings.AUTH_USER_MODEL),
        ),
    ]