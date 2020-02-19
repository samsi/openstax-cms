# Generated by Django 2.2.8 on 2020-02-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0036_partner_formstack_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerCategoryMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesforce_name', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerFieldNameMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesforce_name', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerTypeMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesforce_name', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=255)),
            ],
        ),
    ]