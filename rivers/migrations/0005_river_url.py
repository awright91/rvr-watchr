# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rivers', '0004_auto_20170701_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='river',
            name='url',
            field=models.CharField(default=' ', max_length=250),
        ),
    ]
