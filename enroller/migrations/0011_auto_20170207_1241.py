# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-07 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroller', '0010_auto_20170207_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainsurvey',
            name='entryGrade',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
