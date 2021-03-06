# Generated by Django 2.2.8 on 2020-01-23 17:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200122_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='checked_in',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='first_name',
            field=models.CharField(default='First', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='last_name',
            field=models.CharField(default='Last', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='registration_email',
            field=models.EmailField(default='test@rice.edu', max_length=255),
            preserve_default=False,
        ),
    ]
