from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Prescription
from .serializers import PrescriptionSerializer


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'patient':
            return Prescription.objects.filter(patient__user=user)
        elif user.user_type == 'doctor':
            return Prescription.objects.filter(doctor__user=user)
        elif user.user_type == 'admin':
            return Prescription.objects.all()
        return Prescription.objects.none()