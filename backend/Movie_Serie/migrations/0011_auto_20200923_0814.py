# Generated by Django 3.1.1 on 2020-09-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_Serie', '0010_auto_20200923_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='link_4k',
            field=models.TextField(blank=True, null=True, verbose_name='4k Link'),
        ),
        migrations.AlterField(
            model_name='url',
            name='link_fhd',
            field=models.TextField(blank=True, null=True, verbose_name='Full HD Link'),
        ),
        migrations.AlterField(
            model_name='url',
            name='link_hd',
            field=models.TextField(blank=True, null=True, verbose_name='HD Link'),
        ),
    ]
