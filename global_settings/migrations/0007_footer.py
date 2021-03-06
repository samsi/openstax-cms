# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-22 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('global_settings', '0006_auto_20161213_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supporters', models.CharField(max_length=255)),
                ('copyright', models.CharField(max_length=255)),
                ('ap_statement', models.CharField(max_length=255)),
                ('facebook_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('linkedin_link', models.URLField()),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Footer',
            },
        ),
    ]
