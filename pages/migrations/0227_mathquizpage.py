# Generated by Django 2.2.10 on 2020-02-27 22:18

from django.db import migrations, models
import django.db.models.deletion
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('pages', '0226_auto_20200219_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='MathQuizPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('results', wagtail.core.fields.StreamField([('result', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(help_text='Used by the frontend for Google Analytics.', required=False))])), ('image_alt_text', wagtail.core.blocks.CharBlock()), ('headline', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.TextBlock()), ('partners', pages.models.PartnerChooserBlock())])))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]