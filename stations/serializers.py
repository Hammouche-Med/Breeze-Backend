from rest_framework import serializers
# from region.serializers import RegionSerializer
from .models import Station

 
class StationsSerializer( serializers.ModelSerializer) :
    # region_id = serializers.RelatedField(source='region', read_only=True)
    region_code = serializers.CharField(source='region.code', read_only=True)
    region_name = serializers.CharField(source='region.name', read_only=True)
    class Meta : 
        model = Station
        fields = '__all__'
    
    