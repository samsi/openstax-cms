# Generated by Django 2.0.2 on 2018-11-26 20:24

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0156_auto_20181126_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuspage',
            name='what_cards',
            field=wagtail.core.fields.StreamField([('card', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))])), ('paragraph', wagtail.core.blocks.TextBlock())], icon='placeholder'))]),
        ),
        migrations.AlterField(
            model_name='ap',
            name='row_1',
            field=wagtail.core.fields.StreamField([('column', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))], help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))]),
        ),
        migrations.AlterField(
            model_name='ap',
            name='row_2',
            field=wagtail.core.fields.StreamField([('column', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))], help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))]),
        ),
        migrations.AlterField(
            model_name='card',
            name='cards',
            field=wagtail.core.fields.StreamField([('card', wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))])), ('headline', wagtail.core.blocks.TextBlock(required=False)), ('description', wagtail.core.blocks.TextBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(required=False)), ('button_url', wagtail.core.blocks.CharBlock(required=False))], icon='document'))]),
        ),
        migrations.AlterField(
            model_name='generalpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('tagline', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('multicolumn', wagtail.core.blocks.StreamBlock([('column', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))], help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))], icon='placeholder')), ('html', wagtail.core.blocks.RawHTMLBlock())]),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='row_1',
            field=wagtail.core.fields.StreamField([('column', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))], help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))]),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='row_2',
            field=wagtail.core.fields.StreamField([('column', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))], help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))]),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='row_3',
            field=wagtail.core.fields.StreamField([('column', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))], help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='banner_images',
            field=wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))]))], null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='mobile_banner_images',
            field=wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_1',
            field=wagtail.core.fields.StreamField([('column', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))], help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_2',
            field=wagtail.core.fields.StreamField([('column', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))], help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_3',
            field=wagtail.core.fields.StreamField([('column', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))], help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_4',
            field=wagtail.core.fields.StreamField([('column', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))], help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_5',
            field=wagtail.core.fields.StreamField([('column', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))], help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))]),
        ),
        migrations.AlterField(
            model_name='mappage',
            name='sections_1_cards',
            field=wagtail.core.fields.StreamField([('card', wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))])), ('headline', wagtail.core.blocks.TextBlock(required=False)), ('description', wagtail.core.blocks.TextBlock(required=False))], icon='document'))]),
        ),
        migrations.AlterField(
            model_name='ourimpact',
            name='row_1',
            field=wagtail.core.fields.StreamField([('column', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))], help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))]),
        ),
        migrations.AlterField(
            model_name='support',
            name='row_1',
            field=wagtail.core.fields.StreamField([('column', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock()), ('identifier', wagtail.core.blocks.CharBlock(required=False))], help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))]),
        ),
    ]