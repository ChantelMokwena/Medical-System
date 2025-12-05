from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Doctor, DoctorAvailability
from .serializers import DoctorAvailabilitySerializer, DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'doctor':
            return Doctor.objects.filter(user=user)
        return Doctor.objects.all()

class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'doctor':
            return DoctorAvailability.objects.filter(doctor__user=user)
        return DoctorAvailability.objects.all()