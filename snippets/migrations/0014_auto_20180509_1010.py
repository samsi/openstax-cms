# Generated by Django 2.0.2 on 2018-05-09 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('snippets', '0013_newssources'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsSources',
            new_name='NewsSource',
        ),
    ]
