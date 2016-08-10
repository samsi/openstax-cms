# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-10 16:09
from __future__ import unicode_literals

from django.db import migrations
import pages.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0051_auto_20160809_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highereducation',
            name='row_1',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='row_2',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='row_3',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_1',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_2',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_3',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_4',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_5',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
    ]
