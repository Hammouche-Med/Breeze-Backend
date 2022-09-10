from rest_framework import serializers

from production.serializers import ProductionSerializer
from .models import Station
from region.serializers import RegionSerializer

 
class StationsSerializer( serializers.ModelSerializer) :
    reg =  RegionSerializer(source="region", many=False  , read_only=True)
    METAR =  ProductionSerializer(source="metar", many=False  , read_only=True)
    SYNOP =  ProductionSerializer(source="synop", many=False  , read_only=True)

    class Meta : 
        model = Station
        fields = '__all__'
    
    