# Generated by Django 2.0.2 on 2018-12-03 20:33

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0159_auto_20181203_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualreportpage',
            name='improving_access',
            field=wagtail.core.fields.StreamField([('background_image', pages.models.APIImageChooserBlock(max_num=1)), ('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('give_text', wagtail.core.blocks.CharBlock(max_num=1))]),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='revolution',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('letter_body', wagtail.core.blocks.TextBlock(max_num=1)), ('signature_image', pages.models.APIImageChooserBlock(max_num=1)), ('signature_alt_text', wagtail.core.blocks.CharBlock(max_num=1)), ('signature_text', wagtail.core.blocks.CharBlock(max_num=1)), ('portrait', pages.models.APIImageChooserBlock(max_num=1)), ('portrait_alt_text', wagtail.core.blocks.CharBlock(max_num=1))]),
        ),
    ]