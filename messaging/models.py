from django.db import models
from django.db import models
from accounts.models import User

class Conversation(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_conversations', limit_choices_to={'user_type': 'patient'})
    staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='staff_conversations', limit_choices_to={'user_type__in': ['admin']}, null=True, blank=True)
    subject = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient.username} - {self.subject}"
    
    class Meta:
        ordering = ['-updated_at']

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sender.username}: {self.content[:50]}"
    
    class Meta:
        ordering = ['created_at']
