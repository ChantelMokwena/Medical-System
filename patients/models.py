from django.db import models
from django_cryptography.fields import encrypt
from accounts.models import User


class Patient(models.Model):
    BLOOD_TYPE_CHOICES = (
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES, blank=True, null=True)
    allergies = encrypt(models.TextField(blank=True, null=True))
    medical_history = encrypt(models.TextField(blank=True, null=True))
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"Patient: {self.user.username}"

class MedicalCondition(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='conditions')
    condition_name = models.CharField(max_length=200)
    diagnosed_date = models.DateField(null=True, blank=True)
    severity = models.CharField(max_length=50, choices=[
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    ], default='moderate')
    notes = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.patient.user.username} - {self.condition_name}"
    
    class Meta:
        ordering = ['-created_at']