# Generated by Django 2.0.13 on 2019-06-27 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('errata', '0031_blockedusers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlockedUsers',
            new_name='BlockedUser',
        ),
    ]