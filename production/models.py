from django.db import models

class Production (models.Model):
    name         =   models.CharField(max_length=50)
    start_t      =   models.TimeField(null=True)
    end_t        =   models.TimeField(null=True)
    rate         =   models.IntegerField(null=True)
    type_obs     =   models.CharField(max_length=20)
    is_essential =   models.BooleanField(default=True)
    full_day     =   models.BooleanField(default=False)
    delay_1t     =   models.IntegerField(null=True)       
    delay_2t     =   models.IntegerField(null=True)

    def __str__(self):
        return self.name
