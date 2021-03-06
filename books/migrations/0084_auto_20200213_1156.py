# Generated by Django 2.2.8 on 2020-02-13 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0083_auto_20191113_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='last_updated_pdf',
            field=models.DateTimeField(blank=True, help_text='Last time PDF was revised.', null=True, verbose_name='PDF Content Revision Date'),
        ),
    ]