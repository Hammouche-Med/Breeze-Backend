from rest_framework import serializers
from observation.models import Observation
from stations.serializers import StationsSerializer
 
class ReportSerializer( serializers.ModelSerializer) :
    stat =  StationsSerializer(source="station", many=False  , read_only=True)
    class Meta : 
        model = Observation
        fields = '__all__'
    