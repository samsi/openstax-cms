# Generated by Django 2.2.8 on 2020-02-03 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('pages', '0221_auto_20200203_0954'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EcosystemAllies',
        ),
    ]
