from dataclasses import fields
from rest_framework import serializers
from production.models import Production
from production.serializers import ProductionSerializer
from stations.models import Station
from stations.serializers import StationsSerializer

from .models import Station_Production
from reports import models

 
class Station_ProductionSerializer( serializers.ModelSerializer) :

    # st_oaci = serializers.CharField(source='station.OACI', read_only=True)
    # st_omm = serializers.CharField(source='station.OMM', read_only=True)
    # st_name = serializers.CharField(source='station.name', read_only=True)

    # prod_name = serializers.CharField(source='production.name', read_only=True)
    # prod_schedule = serializers.CharField(source='production.schedule', read_only=True)
    # prod_type = serializers.CharField(source='production.type_obs', read_only=True)

    stat = StationsSerializer(source="station",many=False, read_only=True)
    prod = ProductionSerializer(source="production",many=False  , read_only=True)

    class Meta : 
        model = Station_Production
        fields = ('id','created_date', 'stat', 'prod',)
    

class ReportSerializer(serializers.Serializer):
   comments = serializers.IntegerField()
   likes = serializers.IntegerField()
    