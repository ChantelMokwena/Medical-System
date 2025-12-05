from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import MedicalCondition, Patient
from .serializers import MedicalConditionSerializer, PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'patient':
            return Patient.objects.filter(user=user)
        elif user.user_type == 'doctor':
            return Patient.objects.all()
        elif user.user_type == 'admin':
            return Patient.objects.all()
        return Patient.objects.none()

class MedicalConditionViewSet(viewsets.ModelViewSet):
    queryset = MedicalCondition.objects.all()
    serializer_class = MedicalConditionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'patient':
            return MedicalCondition.objects.filter(patient__user=user)
        elif user.user_type in ['doctor', 'admin']:
            return MedicalCondition.objects.all()
        return MedicalCondition.objects.none()