# Generated by Django 2.2.8 on 2020-01-17 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0033_partner_partner_list_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='video_1',
            field=models.FileField(blank=True, null=True, upload_to='partner_videos/'),
        ),
        migrations.AddField(
            model_name='partner',
            name='video_2',
            field=models.FileField(blank=True, null=True, upload_to='partner_videos/'),
        ),
    ]
