from django.db import models
from datetime import date
from .base import TimestampBaseModel



class Hospital(TimestampBaseModel):
    name = models.CharField(max_length=255)
    facilities = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=10, )
    emergency_ward = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    def __str__(self):
      return self.name
 


