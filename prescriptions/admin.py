from django.contrib import admin
from .models import Prescription

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['medication_name', 'patient', 'doctor', 'dosage', 'created_at']
    list_filter = ['created_at']
    search_fields = ['medication_name', 'patient__user__username', 'doctor__user__username']