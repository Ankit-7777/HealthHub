from django.db import models
import uuid



class TimestampBaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    blocked = models.BooleanField(default=False)

    class Meta:
        abstract = True
    
    def soft_delete(self):
        print(f"Soft deleting {self.name}...")
        self.is_deleted = True
        self.is_active = False
        self.save()

    def restore(self):
        self.is_deleted = False
        self.is_active = True
        self.save()
