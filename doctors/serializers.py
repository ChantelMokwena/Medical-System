from rest_framework import serializers

from accounts.serializers import UserSerializer

from .models import Doctor, DoctorAvailability


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Doctor
        fields = ['id', 'user', 'specialization', 'license_number', 'years_of_experience', 'consultation_fee']

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    day_of_week_display = serializers.CharField(source='get_day_of_week_display', read_only=True)
    
    class Meta:
        model = DoctorAvailability
        fields = ['id', 'doctor', 'day_of_week', 'day_of_week_display', 'start_time', 'end_time', 'is_available']
        read_only_fields = ['id']