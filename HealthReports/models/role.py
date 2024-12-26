from django.db import models
from .base import TimestampBaseModel


class Role(TimestampBaseModel):
    name = models.CharField(max_length=50, unique=True)
    created_by = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,
        related_name='assigned_roles',
        null=True,
        blank=True,
        help_text="The admin who assigned this role."
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'created_by__email']
