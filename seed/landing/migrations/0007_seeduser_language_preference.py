# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-13 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_auto_20170602_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='seeduser',
            name='language_preference',
            field=models.CharField(default=b'en-US', max_length=16),
        ),
    ]