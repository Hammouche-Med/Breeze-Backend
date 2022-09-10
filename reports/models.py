from django.db import models

from stations.models import Station
from production.models import Production

class Station_Production( models.Model ):
    created_date =  models.DateTimeField(auto_now_add=True)

