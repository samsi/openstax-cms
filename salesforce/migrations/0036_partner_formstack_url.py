# Generated by Django 2.2.8 on 2020-01-22 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0035_auto_20200117_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='formstack_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
