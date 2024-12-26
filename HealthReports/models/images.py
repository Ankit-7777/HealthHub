from django.db import models
from .base import TimestampBaseModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Image(TimestampBaseModel):
    """Model to store images associated with multiple models."""
    image = models.ImageField(upload_to='images/')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Image for {self.content_object}"