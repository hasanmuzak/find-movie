# Generated by Django 3.1.1 on 2020-09-22 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_Serie', '0007_auto_20200922_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_or_serie',
            name='short_desc',
            field=models.TextField(default=1, verbose_name='Description'),
            preserve_default=False,
        ),
    ]