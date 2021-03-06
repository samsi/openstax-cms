# Generated by Django 2.0.2 on 2018-04-05 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0010_communityresource_sharedcontent'),
        ('books', '0042_auto_20180403_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSharedContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, null=True)),
                ('link_text', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.ForeignKey(help_text='Manage shared content through snippets.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.SharedContent')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='ally_blurb',
        ),
        migrations.RemoveField(
            model_name='book',
            name='ally_header',
        ),
        migrations.RemoveField(
            model_name='book',
            name='bookstore_blurb',
        ),
        migrations.RemoveField(
            model_name='book',
            name='bookstore_link',
        ),
        migrations.RemoveField(
            model_name='book',
            name='comp_copy_blurb',
        ),
        migrations.RemoveField(
            model_name='book',
            name='errata_blurb',
        ),
        migrations.RemoveField(
            model_name='book',
            name='errata_link',
        ),
        migrations.RemoveField(
            model_name='book',
            name='free_stuff_blurb',
        ),
        migrations.RemoveField(
            model_name='book',
            name='free_stuff_heading',
        ),
        migrations.RemoveField(
            model_name='book',
            name='webinar_blurb',
        ),
        migrations.RemoveField(
            model_name='book',
            name='webinar_heading',
        ),
        migrations.AddField(
            model_name='book',
            name='book_ally',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='books.BookSharedContent'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_errata',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='books.BookSharedContent'),
        ),
        migrations.AddField(
            model_name='book',
            name='bookstore',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='books.BookSharedContent'),
        ),
        migrations.AddField(
            model_name='book',
            name='comp_copy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='books.BookSharedContent'),
        ),
        migrations.AddField(
            model_name='book',
            name='free_stuff_instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='books.BookSharedContent'),
        ),
        migrations.AddField(
            model_name='book',
            name='free_stuff_student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='books.BookSharedContent'),
        ),
        migrations.AddField(
            model_name='book',
            name='webinar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='books.BookSharedContent'),
        ),
    ]
