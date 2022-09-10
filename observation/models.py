from django.db import models

from stations.models import Station

class Observation (models.Model):

    obs_date = models.DateField()
    obs_time = models.TimeField()
    rec_date = models.DateField()
    rec_time = models.TimeField()
    type = models.CharField(max_length=50)
    content = models.CharField(max_length=254)
    station = models.ForeignKey(Station, related_name='station', on_delete=models.CASCADE)

    def __str__(self):
        return self.type

