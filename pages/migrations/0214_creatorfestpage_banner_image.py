# Generated by Django 2.2.5 on 2019-10-09 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('pages', '0213_auto_20191009_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatorfestpage',
            name='banner_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
