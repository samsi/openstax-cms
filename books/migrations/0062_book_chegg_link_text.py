# Generated by Django 2.0.9 on 2018-12-19 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0061_book_chegg_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='chegg_link_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]