#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Area(models.Model):
    zone = models.CharField(max_length=3)
    min_lat = models.FloatField()
    max_lat = models.FloatField()
    min_lon = models.FloatField()
    max_lon = models.FloatField()

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.zone
