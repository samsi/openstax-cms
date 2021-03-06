# Generated by Django 2.0.2 on 2018-07-25 21:13

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import pages.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0129_auto_20180725_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('people', wagtail.core.fields.StreamField((('person', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock()), ('title', wagtail.core.blocks.CharBlock()), ('photo', pages.models.APIImageChooserBlock(required=False))), icon='user')),))),
            ],
        ),
        migrations.CreateModel(
            name='OpenStaxPeople',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Group')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('marketing_video', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='openstax_people', to='pages.TeamPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('pages.group', models.Model),
        ),
    ]
