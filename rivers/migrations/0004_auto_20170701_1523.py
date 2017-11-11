# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rivers', '0003_river_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='river',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='river', to='locations.State'),
        ),
    ]