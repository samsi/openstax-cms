# Generated by Django 2.0.2 on 2018-07-26 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0132_auto_20180726_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='teampage',
            name='team_header',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]