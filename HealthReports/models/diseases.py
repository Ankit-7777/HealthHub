from django.db import models
from .base import TimestampBaseModel


class Diseases(TimestampBaseModel):
    name = models.CharField(max_length=90, unique=True)
    
    def __str__(self):
      return self.name
    
