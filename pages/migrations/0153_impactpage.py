# Generated by Django 2.0.2 on 2018-11-02 14:28

from django.db import migrations, models
import django.db.models.deletion
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0020_add-verbose-name'),
        ('wagtailcore', '0040_page_draft_title'),
        ('pages', '0152_merge_20181029_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImpactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('header_text', models.CharField(max_length=255)),
                ('sections_1_cards', wagtail.core.fields.StreamField([('card', wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())])), ('headline', wagtail.core.blocks.TextBlock(required=False)), ('description', wagtail.core.blocks.TextBlock(required=False))], icon='document'))])),
                ('section_2_header_1', models.CharField(max_length=255)),
                ('section_2_blurb_1', models.TextField()),
                ('sections_2_cta_1', models.CharField(max_length=255)),
                ('section_2_link_1', models.CharField(max_length=255)),
                ('section_2_header_2', models.CharField(max_length=255)),
                ('section_2_blurb_2', models.TextField()),
                ('sections_2_cta_2', models.CharField(max_length=255)),
                ('section_2_link_2', models.CharField(max_length=255)),
                ('section_3_heading', models.CharField(max_length=255)),
                ('section_3_blurb', models.TextField()),
                ('section_3_cta', models.CharField(max_length=255)),
                ('section_3_link', models.CharField(max_length=255)),
                ('promote_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('section_2_image_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('section_2_image_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
