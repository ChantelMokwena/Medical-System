from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models import Count
from accounts.models import User, AuditLog
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from prescriptions.models import Prescription
from messaging.models import Conversation, Message

@staff_member_required
def admin_dashboard(request):
    try:
        context = {
            'total_users': User.objects.count(),
            'total_patients': Patient.objects.count(),
            'total_doctors': Doctor.objects.count(),
            'total_appointments': Appointment.objects.count(),
            'active_prescriptions': Prescription.objects.filter(status='active').count(),
            'total_conversations': Conversation.objects.count(),
            'unread_messages': Message.objects.filter(is_read=False).count(),
            'recent_audit_logs': AuditLog.objects.select_related('user')[:10],
        }
    except Exception as e:
        context = {'error': str(e)}
    
    return render(request, 'admin/dashboard.html', context)