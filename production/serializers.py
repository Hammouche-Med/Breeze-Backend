from unittest import expectedFailure
from rest_framework import serializers
from .models import Production
from datetime import datetime
import calendar
 
class ProductionSerializer( serializers.ModelSerializer) :


    expected_d = serializers.SerializerMethodField('day')
    expected_m = serializers.SerializerMethodField('month')

    def day(self, production):
        t1 = datetime.strptime(str(production.start_t), "%H:%M:%S")
        t2 = datetime.strptime(str(production.end_t), "%H:%M:%S")
        diff = t2-t1
        return diff.total_seconds()/production.rate 
    def month(self, production):
        now = datetime.now()
        t1 = datetime.strptime(str(production.start_t), "%H:%M:%S")
        t2 = datetime.strptime(str(production.end_t), "%H:%M:%S")
        diff = t2-t1
        return diff.total_seconds()/production.rate * calendar.monthrange(now.year, now.month)[1]

    
    class Meta : 
        model = Production
        fields = '__all__'
    