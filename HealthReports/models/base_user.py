from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import date
from .base import TimestampBaseModel
from django.utils import timezone
from django.apps import apps





class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin, TimestampBaseModel):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'  

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]


    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.ImageField(upload_to='user_profiles/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        app_label = "HealthReports"
        db_table = "user_profile"
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
        ordering = ['first_name', 'last_name']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['first_name', 'last_name']),
            models.Index(fields=['role']),
            models.Index(fields=['date_of_birth']),
            models.Index(fields=['is_active']),
        ]


    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def get_short_name(self):
        return self.first_name or self.email.split('@')[0]

    @property
    def age(self):
        return date.today().year - self.date_of_birth.year if self.date_of_birth else None

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        previous_role = None
        if not is_new:
            previous_role = User.objects.get(pk=self.pk).role

        super().save(*args, **kwargs)

        if is_new or (previous_role != self.role and self.role):
            self.handle_role_assignment()

    def handle_role_assignment(self):
        """
        Dynamically handles the creation of associated models based on the user's role.
        The associated model name should match the role name.
        """
        if self.role:
            model_name = self.role.name.replace(' ', '')
            try:
                ModelClass = apps.get_model('HealthReports', model_name)
                if ModelClass:
                    ModelClass.objects.get_or_create(user=self)
            except LookupError:
                print(f"Model '{model_name}' does not exist.")
            except Exception as e:
                print(f"Error while assigning role: {e}")

