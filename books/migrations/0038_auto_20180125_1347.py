# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-25 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0037_book_kindle_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='student_handbook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
    ]