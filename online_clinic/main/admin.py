from django.contrib import admin
from .models import (
    Divisions,
    Patient
)

admin.site.register(Divisions)
admin.site.register(Patient)
