from django.db import models
from datetime import date
from .base import TimestampBaseModel


class Clinic(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15, )
    emergency_ward  = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    def __str__(self):
      return self.name


