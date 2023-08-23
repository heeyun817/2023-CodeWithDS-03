from django.contrib import admin
from channels.models import ChatMessage, ChatRoom
# Register your models here.
admin.site.register(ChatMessage)
admin.site.register(ChatRoom)