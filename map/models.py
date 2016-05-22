# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Area(models.Model):
    zone = models.CharField(max_length=3)
    min_lat = models.FloatField()
    max_lat = models.FloatField()
    min_lon = models.FloatField()
    max_lon = models.FloatField()

    def __str__(self):
        return self.zone


class AreaHand(models.Model):
    # TODO : recharger la base via le csv avant de rendre le projet
    area = models.CharField(max_length=3)
    count = models.IntegerField()
    fortnight = models.IntegerField()
    month = models.IntegerField()
    boatType = models.TextField()
    year = models.IntegerField()
    activity = models.IntegerField()

    def __str__(self):
        return self.zone
