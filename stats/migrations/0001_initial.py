# Generated by Django 3.2 on 2023-02-09 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='DataItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(verbose_name='Value')),
                ('user', models.CharField(max_length=50, verbose_name='User')),
                ('statstic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statistic_dataitems', to='stats.statistic', verbose_name='Statistic')),
            ],
        ),
    ]