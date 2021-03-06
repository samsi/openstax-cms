# Generated by Django 2.0.2 on 2018-12-05 21:15

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0165_auto_20181203_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualreportpage',
            name='disruption',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('graph', wagtail.core.blocks.StructBlock([('top_caption', wagtail.core.blocks.CharBlock(max_num=1)), ('bottom_caption', wagtail.core.blocks.RichTextBlock(max_num=1)), ('image', pages.models.APIImageChooserBlock(max_num=1, required=False)), ('image_alt_text', wagtail.core.blocks.CharBlock(max_num=1, required=False))]))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='giving',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('link_1', wagtail.core.blocks.CharBlock()), ('link_1_text', wagtail.core.blocks.CharBlock())], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='improving_access',
            field=wagtail.core.fields.StreamField([('background_image', pages.models.APIImageChooserBlock(max_num=1)), ('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.RichTextBlock(max_num=1)), ('give_text', wagtail.core.blocks.CharBlock(max_num=1))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='looking_ahead',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('image', pages.models.APIImageChooserBlock(max_num=1))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='map',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('link', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock()), ('background_image', pages.models.APIImageChooserBlock(max_num=1)), ('image_1', pages.models.APIImageChooserBlock(max_num=1)), ('image_2', pages.models.APIImageChooserBlock(max_num=1))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='philanthropic_partners',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('image', pages.models.APIImageChooserBlock(max_num=1)), ('image_alt_text', wagtail.core.blocks.CharBlock()), ('link_1', wagtail.core.blocks.CharBlock()), ('link_1_text', wagtail.core.blocks.CharBlock()), ('link_2', wagtail.core.blocks.CharBlock()), ('link_2_text', wagtail.core.blocks.CharBlock())], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='reach',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.RichTextBlock(max_num=1)), ('facts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('number', wagtail.core.blocks.IntegerBlock(max_num=1)), ('unit', wagtail.core.blocks.CharBlock(max_num=1)), ('text', wagtail.core.blocks.CharBlock(max_num=1))])))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='revolution',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('letter_body', wagtail.core.blocks.RichTextBlock(max_num=1)), ('signature_image', pages.models.APIImageChooserBlock(max_num=1)), ('signature_alt_text', wagtail.core.blocks.CharBlock(max_num=1)), ('signature_text', wagtail.core.blocks.RichTextBlock(max_num=1)), ('portrait', pages.models.APIImageChooserBlock(max_num=1)), ('portrait_alt_text', wagtail.core.blocks.CharBlock(max_num=1))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='tutor',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('link', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock()), ('right_image', pages.models.APIImageChooserBlock(max_num=1)), ('bottom_image', pages.models.APIImageChooserBlock(max_num=1))], null=True),
        ),
    ]
