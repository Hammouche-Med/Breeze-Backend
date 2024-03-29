from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    username = models.CharField(max_length=30, unique=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone']

    def __str__(self):
        return self.email
