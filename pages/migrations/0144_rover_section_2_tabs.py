# Generated by Django 2.0.2 on 2018-10-16 21:18

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0143_auto_20181016_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='rover',
            name='section_2_tabs',
            field=wagtail.core.fields.StreamField([('headline', wagtail.core.blocks.CharBlock()), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.CharBlock()), ('headline', wagtail.core.blocks.TextBlock()), ('description', wagtail.core.blocks.RichTextBlock())])))], null=True),
        ),
    ]
