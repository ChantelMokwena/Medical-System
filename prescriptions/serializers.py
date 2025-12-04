from rest_framework import serializers

from doctors.serializers import DoctorSerializer
from patients.serializers import PatientSerializer

from .models import Prescription


class PrescriptionSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)
    patient_id = serializers.IntegerField(write_only=True)
    doctor_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Prescription
        fields = ['id', 'appointment', 'patient', 'doctor', 'patient_id', 'doctor_id', 'medication_name', 'dosage', 'frequency', 'duration', 'instructions', 'created_at']
        read_only_fields = ['id', 'created_at']