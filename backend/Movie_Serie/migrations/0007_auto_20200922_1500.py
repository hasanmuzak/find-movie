# Generated by Django 3.1.1 on 2020-09-22 15:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_Serie', '0006_auto_20200922_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_or_serie',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie_or_serie',
            name='production_year',
            field=models.CharField(default=1, max_length=4, verbose_name='Production Year'),
            preserve_default=False,
        ),
    ]
