# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('global_settings', '0011_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='site',
        ),
        migrations.DeleteModel(
            name='Mail',
        ),
    ]