# Generated by Django 2.0.2 on 2018-04-09 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0052_auto_20180406_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcommunityresources',
            name='book_community_resource',
        ),
        migrations.RemoveField(
            model_name='bookcommunityresources',
            name='communityresources_ptr',
        ),
        migrations.RemoveField(
            model_name='communityresources',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='communityresources',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='communityresources',
            name='resource',
        ),
        migrations.RemoveField(
            model_name='book',
            name='community_resource_content',
        ),
        migrations.DeleteModel(
            name='BookCommunityResources',
        ),
        migrations.DeleteModel(
            name='CommunityResources',
        ),
    ]
