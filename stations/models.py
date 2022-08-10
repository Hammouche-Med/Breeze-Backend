from django.db import models

from region.models import Region


class Station (models.Model):
    OACI = models.CharField(max_length=50)
    OMM = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    longitude = models.FloatField(max_length=100)
    latitude = models.FloatField(max_length=100)
    altitude = models.FloatField(max_length=100)

    region = models.ForeignKey(Region, related_name='region', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
