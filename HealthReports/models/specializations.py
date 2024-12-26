from django.db import models
from .base import TimestampBaseModel



class Specialization(TimestampBaseModel):
    """Dynamic model to store specializations."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name