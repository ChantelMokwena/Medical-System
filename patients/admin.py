from django.contrib import admin

from .models import MedicalCondition, Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'blood_type', 'emergency_contact_name']
    search_fields = ['user__username', 'user__email']

@admin.register(MedicalCondition)
class MedicalConditionAdmin(admin.ModelAdmin):
    list_display = ['patient', 'condition_name', 'severity', 'diagnosed_date', 'is_active']
    list_filter = ['severity', 'is_active']
    search_fields = ['patient__user__username', 'condition_name']