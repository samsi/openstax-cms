# Generated by Django 2.0.2 on 2018-12-03 22:19

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0164_auto_20181203_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualreportpage',
            name='giving',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.RichTextBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('link_1', wagtail.core.blocks.CharBlock()), ('link_1_text', wagtail.core.blocks.CharBlock())], null=True),
        ),
        migrations.AddField(
            model_name='annualreportpage',
            name='looking_ahead',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.RichTextBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('image', pages.models.APIImageChooserBlock(max_num=1))], null=True),
        ),
        migrations.AddField(
            model_name='annualreportpage',
            name='map',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.RichTextBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('link', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock()), ('background_image', pages.models.APIImageChooserBlock(max_num=1)), ('image_1', pages.models.APIImageChooserBlock(max_num=1)), ('image_2', pages.models.APIImageChooserBlock(max_num=1))], null=True),
        ),
        migrations.AddField(
            model_name='annualreportpage',
            name='philanthropic_partners',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.RichTextBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('image', pages.models.APIImageChooserBlock(max_num=1)), ('image_alt_text', wagtail.core.blocks.CharBlock()), ('link_1', wagtail.core.blocks.CharBlock()), ('link_1_text', wagtail.core.blocks.CharBlock()), ('link_2', wagtail.core.blocks.CharBlock()), ('link_2_text', wagtail.core.blocks.CharBlock())], null=True),
        ),
        migrations.AddField(
            model_name='annualreportpage',
            name='tutor',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.RichTextBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('link', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock()), ('right_image', pages.models.APIImageChooserBlock(max_num=1)), ('bottom_image', pages.models.APIImageChooserBlock(max_num=1))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='disruption',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('graph', wagtail.core.blocks.StructBlock([('top_caption', wagtail.core.blocks.CharBlock(max_num=1)), ('bottom_caption', wagtail.core.blocks.RawHTMLBlock(max_num=1)), ('image', pages.models.APIImageChooserBlock(max_num=1, required=False)), ('image_alt_text', wagtail.core.blocks.CharBlock(max_num=1, required=False))]))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='sustainability',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('partners', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', pages.models.APIImageChooserBlock(max_num=1, required=False)), ('image_alt_text', wagtail.core.blocks.CharBlock(max_num=1))])))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='testimonials',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('testimonials', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', pages.models.APIImageChooserBlock(max_num=1, required=False)), ('image_alt_text', wagtail.core.blocks.CharBlock(max_num=1)), ('quote', wagtail.core.blocks.CharBlock(max_num=1)), ('link', wagtail.core.blocks.URLBlock(max_num=1)), ('link_text', wagtail.core.blocks.CharBlock(max_num=1))])))], null=True),
        ),
    ]
