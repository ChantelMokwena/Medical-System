from rest_framework import serializers

from accounts.serializers import UserSerializer

from .models import MedicalCondition, Patient


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Patient
        fields = ['id', 'user', 'blood_type', 'allergies', 'medical_history', 'emergency_contact', 'emergency_contact_name']

class MedicalConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCondition
        fields = ['id', 'patient', 'condition_name', 'diagnosed_date', 'severity', 'notes', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']