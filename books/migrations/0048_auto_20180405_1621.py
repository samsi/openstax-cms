# Generated by Django 2.0.2 on 2018-04-05 21:21

import books.models
from django.db import migrations
import snippets.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0047_auto_20180405_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ally_content',
            field=wagtail.core.fields.StreamField((('content', books.models.SharedContentChooserBlock(snippets.models.SharedContent)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(required=False))), null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookstore_content',
            field=wagtail.core.fields.StreamField((('content', books.models.SharedContentChooserBlock(snippets.models.SharedContent)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(required=False))), null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='comp_copy_content',
            field=wagtail.core.fields.StreamField((('content', books.models.SharedContentChooserBlock(snippets.models.SharedContent)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(required=False))), null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='errata_content',
            field=wagtail.core.fields.StreamField((('content', books.models.SharedContentChooserBlock(snippets.models.SharedContent)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(required=False))), null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='free_stuff_instructor',
            field=wagtail.core.fields.StreamField((('content', books.models.SharedContentChooserBlock(snippets.models.SharedContent)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(required=False))), null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='free_stuff_student',
            field=wagtail.core.fields.StreamField((('content', books.models.SharedContentChooserBlock(snippets.models.SharedContent)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(required=False))), null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='webinar_content',
            field=wagtail.core.fields.StreamField((('content', books.models.SharedContentChooserBlock(snippets.models.SharedContent)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(required=False))), null=True),
        ),
    ]
