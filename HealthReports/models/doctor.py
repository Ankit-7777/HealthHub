from django.db import models
from datetime import date
from .base import TimestampBaseModel
from django.utils import timezone



class Doctor(TimestampBaseModel):
    """Doctor model with dynamic qualifications and specializations."""
    BLOOD_GROUP_CHOICES = [
        ('A Positive (A+)', 'A Positive (A+)'),
        ('A Negative (A-)', 'A Negative (A-)'),
        ('B Positive (B+)', 'B Positive (B+)'),
        ('B Negative (B-)', 'B Negative (B-)'),
        ('O Positive (O+)', 'O Positive (O+)'),
        ('O Negative (O-)', 'O Negative (O-)'),
        ('AB Positive (AB+)', 'AB Positive (AB+)'),
        ('AB Negative (AB-)', 'AB Negative (AB-)'),
    ]

    
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    user = models.OneToOneField(
        'User',
        on_delete=models.CASCADE,
        related_name="doctor_profile",
        limit_choices_to={'role__name__iexact': 'doctor'}
    )
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    qualifications = models.ManyToManyField('Qualification', related_name="doctors")
    specializations = models.ManyToManyField('Specialization', related_name="doctors")
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE, related_name='doctors')
    clinic = models.ForeignKey('Clinic', on_delete=models.CASCADE, related_name='doctors')
    documents = models.ManyToManyField('Document', related_name='doctor_documents')
    images = models.ManyToManyField('Image', related_name='doctor_images')
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    blood_group = models.CharField(max_length=20, choices=BLOOD_GROUP_CHOICES, null=True)
    
    def __str__(self):
        return f"Doctor {self.id}"
