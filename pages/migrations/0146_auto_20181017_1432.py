# Generated by Django 2.0.2 on 2018-10-17 19:32

from django.db import migrations, models
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0145_auto_20181016_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='rover',
            name='section_3_cards',
            field=wagtail.core.fields.StreamField([('headline', wagtail.core.blocks.CharBlock()), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())])), ('description', wagtail.core.blocks.RichTextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_url', wagtail.core.blocks.URLBlock())])))], null=True),
        ),
        migrations.AddField(
            model_name='rover',
            name='section_3_description',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='rover',
            name='section_3_headline',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rover',
            name='section_4_faqs',
            field=wagtail.core.fields.StreamField([('headline', wagtail.core.blocks.CharBlock()), ('faqs', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('question', wagtail.core.blocks.CharBlock()), ('answer', wagtail.core.blocks.TextBlock())])))], null=True),
        ),
        migrations.AddField(
            model_name='rover',
            name='section_4_headline',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
