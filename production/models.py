from django.db import models

class Production (models.Model):
    name  =           models.CharField(max_length=254)
    time_meter  =     models.CharField(max_length=254)
    schedule  =       models.CharField(max_length=254)
    type_obs  =       models.CharField(max_length=254)
    expected_d  =     models.IntegerField(null=True)
    expected_m  =     models.IntegerField(null=True)
    expected_s  =     models.IntegerField(null=True)
    expected_y  =     models.IntegerField(null=True)
    delay_1t  =       models.IntegerField(null=True)       
    delay_2t  =       models.IntegerField(null=True)
    delay_3t  =       models.IntegerField(null=True)

    def __str__(self):
        return self.name
