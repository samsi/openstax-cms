# Generated by Django 2.0.2 on 2018-05-08 13:50

from django.db import migrations, models
import django.db.models.deletion
import wagtail.search.index


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('snippets', '0012_auto_20180418_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsSources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
    ]