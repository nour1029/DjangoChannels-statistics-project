# Generated by Django 4.1.6 on 2023-02-10 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='Slug'),
        ),
    ]