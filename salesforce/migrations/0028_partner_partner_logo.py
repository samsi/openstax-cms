# Generated by Django 2.2.5 on 2019-12-19 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0027_auto_20191122_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='partner_logo',
            field=models.ImageField(blank=True, null=True, upload_to='partner_logos/'),
        ),
    ]
