# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfs', '0012_auto_20170926_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('forecast_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('forecast_rns', models.FloatField()),
                ('forecast_arr', models.FloatField()),
                ('forecast_rev', models.FloatField()),
                ('actual_reference', models.ManyToManyField(to='rfs.Actual')),
            ],
        ),
    ]
