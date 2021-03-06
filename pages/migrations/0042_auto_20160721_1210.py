# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 17:10
from __future__ import unicode_literals

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0041_auto_20160721_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='row_2',
            field=wagtail.core.fields.StreamField((('multicolumn', wagtail.core.blocks.StreamBlock((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_3',
            field=wagtail.core.fields.StreamField((('multicolumn', wagtail.core.blocks.StreamBlock((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_4',
            field=wagtail.core.fields.StreamField((('multicolumn', wagtail.core.blocks.StreamBlock((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_5',
            field=wagtail.core.fields.StreamField((('multicolumn', wagtail.core.blocks.StreamBlock((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),))),)),
        ),
    ]
