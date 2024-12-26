from django.contrib import admin
from .models import (
    Address,
    Role,
    Clinic,
    Hospital,
    Diseases,
    Doctor,
    Document,
    Image,
    Patient,
    Qualification,
    Specialization,
    User
)

admin.site.register([
    Address,
    Role,
    Clinic,
    Hospital,
    Diseases,
    Doctor,
    Document,
    Image,
    Patient,
    Qualification,
    Specialization,
    User
])

