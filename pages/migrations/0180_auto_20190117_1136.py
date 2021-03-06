# Generated by Django 2.0.9 on 2019-01-17 17:36

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0179_auto_20190114_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roverpage',
            name='section_2',
            field=wagtail.core.fields.StreamField([('video', wagtail.core.blocks.RawHTMLBlock()), ('heading', wagtail.core.blocks.CharBlock()), ('subheading', wagtail.core.blocks.TextBlock())]),
        ),
        migrations.AlterField(
            model_name='roverpage',
            name='section_4',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('blurb', wagtail.core.blocks.TextBlock()), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('blurb', wagtail.core.blocks.TextBlock()), ('image', pages.models.APIImageChooserBlock()), ('image_alt_text', wagtail.core.blocks.CharBlock())])))]),
        ),
        migrations.AlterField(
            model_name='roverpage',
            name='section_6',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('blurb', wagtail.core.blocks.RichTextBlock()), ('image', pages.models.APIImageChooserBlock()), ('image_alt_text', wagtail.core.blocks.CharBlock()), ('caption', wagtail.core.blocks.CharBlock())]),
        ),
    ]
