from rest_framework import serializers

from production.serializers import ProductionSerializer
from .models import Station
from region.serializers import RegionSerializer

 
class StationsSerializer( serializers.ModelSerializer) :
    reg =  RegionSerializer(source="region", many=False  , read_only=True)
    mtr =  ProductionSerializer(source="metar", many=False  , read_only=True)
    snp =  ProductionSerializer(source="synop", many=False  , read_only=True)

    calculated_feild = serializers.SerializerMethodField('num')
    def num(self, station):
      return station.altitude * station.longitude 

    class Meta : 
        model = Station
        fields = '__all__'
    
    