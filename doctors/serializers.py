from rest_framework import serializers

from accounts.serializers import UserSerializer

from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Doctor
        fields = ['id', 'user', 'specialisation', 'license_number', 'years_of_experience', 'consultation_fee']