from django.db import models

from stations.models import Station
from production.models import Production

class Station_Production( models.Model ):

    station = models.ForeignKey(Station, related_name='stat', on_delete=models.CASCADE)
    production = models.ForeignKey(Production, related_name='prod', on_delete=models.CASCADE)
    created_date =  models.DateTimeField(auto_now_add=True)

