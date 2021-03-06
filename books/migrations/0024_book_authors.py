# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-19 18:57
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0023_auto_20160622_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=wagtail.core.fields.StreamField((('author', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(required=True)), ('university', wagtail.core.blocks.CharBlock()), ('country', wagtail.core.blocks.CharBlock()), ('senior_author', wagtail.core.blocks.BooleanBlock()), ('display_at_top', wagtail.core.blocks.BooleanBlock())))),), blank=True, null=True),
        ),
    ]
