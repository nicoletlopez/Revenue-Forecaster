# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import rfs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actual',
            fields=[
                ('actual_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('actual_rns', models.DecimalField(decimal_places=2, max_digits=15)),
                ('actual_arr', models.DecimalField(decimal_places=2, max_digits=15)),
                ('actual_rev', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            options={
                'ordering': ['actual_id'],
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel_file', models.FileField(upload_to=rfs.models.project_directory_path)),
                ('status', models.CharField(choices=[('ARC', 'Archived'), ('ACT', 'Active')], default='ACT', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('forecast_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('forecast_rns', models.DecimalField(decimal_places=2, max_digits=15)),
                ('forecast_arr', models.DecimalField(decimal_places=2, max_digits=15)),
                ('forecast_rev', models.DecimalField(decimal_places=2, max_digits=15)),
                ('actual_reference', models.ManyToManyField(to='rfs.Actual')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('ARC', 'Archived'), ('ACT', 'Active')], default='ACT', max_length=3)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Seg_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('seg_type', models.CharField(choices=[('IND', 'Individual'), ('GRP', 'Group')], max_length=30)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Grp_seg',
            fields=[
                ('grp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='rfs.Seg_list')),
                ('tag', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['grp_id'],
            },
        ),
        migrations.CreateModel(
            name='Ind_seg',
            fields=[
                ('ind', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='rfs.Seg_list')),
                ('tag', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['ind_id'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='seg_list',
            unique_together=set([('tag', 'name')]),
        ),
        migrations.AddField(
            model_name='file',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfs.Project'),
        ),
        migrations.AddField(
            model_name='actual',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfs.Project'),
        ),
        migrations.AddField(
            model_name='actual',
            name='segment',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='rfs.Seg_list'),
        ),
    ]
