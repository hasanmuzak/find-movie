# Generated by Django 3.1.1 on 2020-09-22 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_Serie', '0002_auto_20200922_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Status')),
            ],
        ),
        migrations.AlterField(
            model_name='movie_or_serie',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movie_Serie.status'),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]