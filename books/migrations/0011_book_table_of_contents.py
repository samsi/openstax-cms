# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-15 15:00
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20160309_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='table_of_contents',
            field=jsonfield.fields.JSONField(blank=True, editable=False),
        ),
    ]