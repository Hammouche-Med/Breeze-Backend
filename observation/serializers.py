from rest_framework import serializers
from .models import Observation
 
class ObservationSerializer( serializers.ModelSerializer) :
    station_name = serializers.CharField(source='station.name', read_only=True)
    station_oaci = serializers.CharField(source='station.OACI', read_only=True)
    station_omm = serializers.CharField(source='station.OMM', read_only=True)
    class Meta : 
        model = Observation
        fields = '__all__'
    