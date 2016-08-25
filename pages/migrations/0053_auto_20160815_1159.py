# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-15 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0052_auto_20160810_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecosystemallies',
            name='classroom_text',
        ),
        migrations.AddField(
            model_name='ecosystemallies',
            name='page_description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='adopt_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='get_started_step_1_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='get_started_step_2_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='get_started_step_3_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='intro_description',
            field=models.TextField(),
        ),
    ]