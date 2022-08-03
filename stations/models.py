from django.db import models


class Station (models.Model):
    OACI = models.CharField(max_length=50)
    OMM = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    longitude = models.FloatField(max_length=100)
    latitude = models.FloatField(max_length=100)
    altitude = models.FloatField(max_length=100)

    def __str__(self):
        return self.name
