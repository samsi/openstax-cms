# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-06 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickynote',
            name='show_sticky',
            field=models.NullBooleanField(),
        ),
    ]
