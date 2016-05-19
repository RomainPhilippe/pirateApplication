# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20160519_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areahand',
            name='id_zone',
        ),
        migrations.AlterField(
            model_name='areahand',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Area'),
        ),
    ]
