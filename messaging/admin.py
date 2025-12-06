from django.contrib import admin
from .models import Conversation, Message

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['patient', 'staff', 'subject', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['patient__username', 'staff__username', 'subject']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['conversation', 'sender', 'content_preview', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['sender__username', 'content']
    
    def content_preview(self, obj):
        return obj.content[:50]
    content_preview.short_description = 'Content'
