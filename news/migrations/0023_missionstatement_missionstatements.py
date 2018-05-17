# Generated by Django 2.0.2 on 2018-05-15 21:12

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0022_auto_20180515_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissionStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MissionStatements',
            fields=[
                ('missionstatement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='news.MissionStatement')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('mission_statements', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='mission_statements', to='news.PressIndex')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('news.missionstatement', models.Model),
        ),
    ]
