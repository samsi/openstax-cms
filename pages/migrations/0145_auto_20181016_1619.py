# Generated by Django 2.0.2 on 2018-10-16 21:19

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0144_rover_section_2_tabs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rover',
            name='section_2_tabs',
            field=wagtail.core.fields.StreamField([('headline', wagtail.core.blocks.CharBlock()), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())])), ('headline', wagtail.core.blocks.TextBlock()), ('description', wagtail.core.blocks.RichTextBlock())])))], null=True),
        ),
    ]