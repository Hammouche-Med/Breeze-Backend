from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    username = models.CharField(max_length=254, unique=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone']

    def __str__(self):
        return self.email
