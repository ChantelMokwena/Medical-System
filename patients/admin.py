from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'blood_type', 'emergency_contact_name']
    search_fields = ['user__username', 'user__email']