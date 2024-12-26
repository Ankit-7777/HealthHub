from django.db import models
from .base import TimestampBaseModel

class Qualification(TimestampBaseModel):
    """Dynamic model to store qualifications."""
    AWARDED_MONTH_CHOICES = [
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    ]
    name = models.CharField(max_length=100, unique=True)
    awarded_year = models.PositiveIntegerField()
    awarded_month = models.PositiveIntegerField(choices=AWARDED_MONTH_CHOICES)

    def __str__(self):
        return self.name
