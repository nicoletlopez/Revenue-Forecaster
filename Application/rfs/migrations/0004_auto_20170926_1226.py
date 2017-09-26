# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 04:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfs', '0003_group_segment_master_individual_segment_master_segmentation_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group_segment_master',
            name='GRP_SEG_ID',
        ),
        migrations.RemoveField(
            model_name='individual_segment_master',
            name='IND_SEG_ID',
        ),
        migrations.DeleteModel(
            name='GROUP_SEGMENT_MASTER',
        ),
        migrations.DeleteModel(
            name='INDIVIDUAL_SEGMENT_MASTER',
        ),
        migrations.DeleteModel(
            name='SEGMENTATION_LIST',
        ),
    ]