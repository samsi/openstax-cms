# Generated by Django 2.2.10 on 2020-02-21 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0037_partnercategorymapping_partnerfieldnamemapping_partnertypemapping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partnertypemapping',
            name='salesforce_name',
        ),
    ]
