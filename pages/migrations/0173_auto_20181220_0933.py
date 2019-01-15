# Generated by Django 2.0.9 on 2018-12-20 15:33

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0172_auto_20181217_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualreportpage',
            name='disruption',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('graph', wagtail.core.blocks.StructBlock([('top_caption', wagtail.core.blocks.CharBlock(max_num=1)), ('bottom_caption', wagtail.core.blocks.RichTextBlock(max_num=1)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))], max_num=1, required=False)), ('image_alt_text', wagtail.core.blocks.CharBlock(max_num=1, required=False))]))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='founding',
            field=wagtail.core.fields.StreamField([('caption', wagtail.core.blocks.RichTextBlock(max_num=1)), ('portrait', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))], max_num=1)), ('portrait_alt_text', wagtail.core.blocks.CharBlock(max_num=1)), ('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='improving_access',
            field=wagtail.core.fields.StreamField([('background_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))], max_num=1)), ('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.RichTextBlock(max_num=1)), ('give_text', wagtail.core.blocks.CharBlock(max_num=1))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='looking_ahead',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))], max_num=1))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='map',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('link', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock()), ('background_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))], max_num=1)), ('image_1', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))], max_num=1)), ('image_2', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))], max_num=1))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='philanthropic_partners',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))], max_num=1)), ('image_alt_text', wagtail.core.blocks.CharBlock()), ('link_1', wagtail.core.blocks.CharBlock()), ('link_1_text', wagtail.core.blocks.CharBlock()), ('link_2', wagtail.core.blocks.CharBlock()), ('link_2_text', wagtail.core.blocks.CharBlock())], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='revolution',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('letter_body', wagtail.core.blocks.RichTextBlock(max_num=1)), ('signature_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))], max_num=1)), ('signature_alt_text', wagtail.core.blocks.CharBlock(max_num=1)), ('signature_text', wagtail.core.blocks.RichTextBlock(max_num=1)), ('portrait', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))], max_num=1)), ('portrait_alt_text', wagtail.core.blocks.CharBlock(max_num=1))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='sustainability',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('partners', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))], max_num=1, required=False)), ('image_alt_text', wagtail.core.blocks.CharBlock(max_num=1))])))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='testimonials',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('testimonials', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))], max_num=1, required=False)), ('image_alt_text', wagtail.core.blocks.CharBlock(max_num=1)), ('quote', wagtail.core.blocks.CharBlock(max_num=1)), ('link', wagtail.core.blocks.URLBlock(max_num=1)), ('link_text', wagtail.core.blocks.CharBlock(max_num=1))])))], null=True),
        ),
        migrations.AlterField(
            model_name='annualreportpage',
            name='tutor',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(max_num=1)), ('description', wagtail.core.blocks.TextBlock(max_num=1)), ('link', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock()), ('right_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))], max_num=1)), ('bottom_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))], max_num=1))], null=True),
        ),
    ]