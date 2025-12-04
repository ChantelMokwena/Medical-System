from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'patient':
            return Appointment.objects.filter(patient__user=user)
        elif user.user_type == 'doctor':
            return Appointment.objects.filter(doctor__user=user)
        elif user.user_type == 'admin':
            return Appointment.objects.all()
        return Appointment.objects.none()
    
    def perform_create(self, serializer):
        serializer.save()