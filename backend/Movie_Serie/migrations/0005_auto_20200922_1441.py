# Generated by Django 3.1.1 on 2020-09-22 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_Serie', '0004_auto_20200922_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='link',
        ),
        migrations.RemoveField(
            model_name='url',
            name='movie_or_serie_title',
        ),
        migrations.AddField(
            model_name='url',
            name='available_4k',
            field=models.BooleanField(default=False, verbose_name='4K Available'),
        ),
        migrations.AddField(
            model_name='url',
            name='available_fhd',
            field=models.BooleanField(default=False, verbose_name='4K Available'),
        ),
        migrations.AddField(
            model_name='url',
            name='available_hd',
            field=models.BooleanField(default=False, verbose_name='4K Available'),
        ),
        migrations.AddField(
            model_name='url',
            name='link_4k',
            field=models.TextField(default=1, unique=True, verbose_name='4k Link'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='url',
            name='link_fhd',
            field=models.TextField(default=1, unique=True, verbose_name='Full HD Link'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='url',
            name='link_hd',
            field=models.TextField(default=1, unique=True, verbose_name='HD Link'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='url',
            name='movie_or_serie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Movie_Serie.movie_or_serie'),
            preserve_default=False,
        ),
    ]
