# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-02 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0033_auto_20170414_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tutor_marketing_book',
            field=models.BooleanField(default=False),
        ),
    ]