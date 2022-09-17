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
        if production.is_essential == True:
            return round (diff.total_seconds()/production.rate , 0)
        else:
            return round( (diff.total_seconds()/production.rate) - (diff.total_seconds()/10800), 0)

    def month(self, production):
        now = datetime.now()
        t1 = datetime.strptime(str(production.start_t), "%H:%M:%S")
        t2 = datetime.strptime(str(production.end_t), "%H:%M:%S")
        diff = t2-t1
        if production.is_essential == True:
            return round( diff.total_seconds()/production.rate * calendar.monthrange(now.year, now.month)[1], 0)
        else:
            return round( (diff.total_seconds()/production.rate * calendar.monthrange(now.year, now.month)[1]) - (diff.total_seconds()/10800 * calendar.monthrange(now.year, now.month)[1]), 0)

    
    class Meta : 
        model = Production
        fields = '__all__'
    