from django.db import models
from datetime import date
from .base import TimestampBaseModel
from django.utils import timezone





class Patient(models.Model):

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

    user = models.OneToOneField(
        'User',
        on_delete=models.CASCADE,
        related_name="patient_profile",
        limit_choices_to={'role__name__iexact': 'patient'}
    )
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    blocked = models.BooleanField(default=False)
    blood_group = models.CharField(max_length=23, choices=BLOOD_GROUP_CHOICES)
    emergency_contact_number = models.CharField(max_length=15)
    emergency_contact_name = models.CharField(max_length=15)
    diseases = models.ManyToManyField('Diseases', blank=True)
    documents = models.ManyToManyField('Document', related_name='patient_documents')
    images = models.ManyToManyField('Image', related_name='patient_images')
    def __str__(self):
        if self.diseases.exists():
            return f'{self.user.first_name} {self.user.last_name} - Diseases: {", ".join([str(d) for d in self.diseases.all()])}'
        else:
            return f'{self.user.first_name} {self.user.last_name} - No diseases'


    @property
    def age(self):
        if self.date_of_birth:
            today = datetime.today().date()
            birthdate = datetime.strptime(str(self.user.date_of_birth), "%Y-%m-%d").date()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            return age
        return None     
 