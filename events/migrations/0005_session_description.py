# Generated by Django 2.2.8 on 2020-01-23 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20200123_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]