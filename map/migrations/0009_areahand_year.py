# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_areahand'),
    ]

    operations = [
        migrations.AddField(
            model_name='areahand',
            name='year',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]