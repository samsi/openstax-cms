# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-18 16:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0103_auto_20171214_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketing',
            name='section_5_dollar_1_paragraph',
        ),
        migrations.RemoveField(
            model_name='marketing',
            name='section_5_dollar_2_paragraph',
        ),
        migrations.RemoveField(
            model_name='marketing',
            name='section_5_dollar_3_paragraph',
        ),
        migrations.RemoveField(
            model_name='marketing',
            name='section_5_dollar_4_paragraph',
        ),
    ]
