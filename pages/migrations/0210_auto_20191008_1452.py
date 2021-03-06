# Generated by Django 2.2.5 on 2019-10-08 19:52

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0209_auto_20191008_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creatorfestpage',
            name='page_panels',
            field=wagtail.core.fields.StreamField([('panel', wagtail.core.blocks.StructBlock([('superheading', wagtail.core.blocks.CharBlock()), ('heading', wagtail.core.blocks.CharBlock()), ('background_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))])), ('video', wagtail.core.blocks.RawHTMLBlock(required=False)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))])), ('headline', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock())])))]))], null=True),
        ),
    ]
