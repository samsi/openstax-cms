# Generated by Django 2.0.2 on 2018-07-17 21:04

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0126_auto_20180716_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuspage',
            name='what_cards',
            field=wagtail.core.fields.StreamField((('card', wagtail.core.blocks.StreamBlock((('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('paragraph', wagtail.core.blocks.TextBlock())), icon='placeholder')),)),
        ),
        migrations.AlterField(
            model_name='ap',
            name='row_1',
            field=wagtail.core.fields.StreamField((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='ap',
            name='row_2',
            field=wagtail.core.fields.StreamField((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='generalpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('tagline', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('multicolumn', wagtail.core.blocks.StreamBlock((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),), icon='placeholder')), ('html', wagtail.core.blocks.RawHTMLBlock()))),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='row_1',
            field=wagtail.core.fields.StreamField((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='row_2',
            field=wagtail.core.fields.StreamField((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='row_3',
            field=wagtail.core.fields.StreamField((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='banner_images',
            field=wagtail.core.fields.StreamField((('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))),), null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_1',
            field=wagtail.core.fields.StreamField((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_2',
            field=wagtail.core.fields.StreamField((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_3',
            field=wagtail.core.fields.StreamField((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_4',
            field=wagtail.core.fields.StreamField((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_5',
            field=wagtail.core.fields.StreamField((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='ourimpact',
            name='row_1',
            field=wagtail.core.fields.StreamField((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='support',
            name='row_1',
            field=wagtail.core.fields.StreamField((('column', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))))),)),
        ),
    ]