# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_communityresource'),
        ('books', '0021_auto_20160531_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_external', models.URLField(blank=True, verbose_name='External link')),
                ('link_text', models.CharField(help_text='Call to Action Text', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BookCommunityResources',
            fields=[
                ('communityresources_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.CommunityResources')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('book_community_resource', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_community_resources', to='books.Book')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('books.communityresources', models.Model),
        ),
        migrations.AddField(
            model_name='communityresources',
            name='resource',
            field=models.ForeignKey(help_text='Manage resources through snippets.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='snippets.CommunityResource'),
        ),
    ]