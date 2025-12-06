from django.contrib import admin
from .models import Prescription

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['medication_name', 'patient', 'doctor', 'status', 'refills_remaining', 'expiry_date', 'created_at']
    list_filter = ['status', 'created_at', 'expiry_date']
    search_fields = ['medication_name', 'patient__user__username', 'doctor__user__username']