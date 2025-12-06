from rest_framework import serializers
from .models import Conversation, Message
from accounts.serializers import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    sender_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Message
        fields = ['id', 'conversation', 'sender', 'sender_id', 'content', 'is_read', 'read_at', 'created_at']
        read_only_fields = ['id', 'created_at', 'read_at']

class ConversationSerializer(serializers.ModelSerializer):
    patient = UserSerializer(read_only=True)
    staff = UserSerializer(read_only=True)
    patient_id = serializers.IntegerField(write_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    unread_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Conversation
        fields = ['id', 'patient', 'staff', 'patient_id', 'subject', 'is_active', 'messages', 'unread_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_unread_count(self, obj):
        return obj.messages.filter(is_read=False).count()