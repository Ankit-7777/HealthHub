from django.db import models
from .base import TimestampBaseModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Address(TimestampBaseModel):
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        ordering = ['country', 'state', 'city']

    HOME = 'home'
    OFFICE = 'office'
    OTHER = 'other'

    ADDRESS_TYPE_CHOICES = [
        (HOME, 'Home'),
        (OFFICE, 'Office'),
        (OTHER, 'Other'),
    ]

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    address_type = models.CharField(
        max_length=10,
        choices=ADDRESS_TYPE_CHOICES,
        default=HOME
    )
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=15)
    additional_details = models.TextField(blank=True, null=True)



    def __str__(self):
        address_type = dict(self.ADDRESS_TYPE_CHOICES).get(self.address_type, "Unknown")
        return f"{self.street_address}, {self.city}, {self.state} ({address_type})"
