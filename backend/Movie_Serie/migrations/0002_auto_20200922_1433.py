# Generated by Django 3.1.1 on 2020-09-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_Serie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=40, unique=True, verbose_name='Title'),
        ),
    ]