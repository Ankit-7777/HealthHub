from django.db import models
from .base import TimestampBaseModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class Document(TimestampBaseModel):
    """Model to store documents associated with multiple models."""
    document = models.FileField(upload_to='documents/')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Document for {self.content_object}"

    def __str__(self):
        return f"Document {self.id}"