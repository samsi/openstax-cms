# Generated by Django 2.0.2 on 2018-12-11 20:12

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0166_auto_20181205_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('tagline', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', pages.models.APIImageChooserBlock()), ('multicolumn', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.RichTextBlock())], icon='placeholder')), ('html', wagtail.core.blocks.RawHTMLBlock())]),
        ),
    ]