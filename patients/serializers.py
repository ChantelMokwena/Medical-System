from rest_framework import serializers

from accounts.serializers import UserSerializer

from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Patient
        fields = ['id', 'user', 'blood_type', 'allergies', 'medical_history', 'emergency_contact', 'emergency_contact_name']