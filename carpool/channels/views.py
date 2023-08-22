from django.shortcuts import render, HttpResponse
from .models import ChatMessage
import json

def chat_view(request):
    messages = ChatMessage.objects.all()
    context = {'messages': messages}
    return render(request, 'chat.html', context)

def send_message(request):
    if request.method == "POST":
        sender = "User"  # Change this to the actual sender (e.g., user's username)
        message = request.POST.get("message")
        ChatMessage.objects.create(sender=sender, message=message)
        return HttpResponse("Message sent successfully.")
    return HttpResponse("Invalid request.")

def get_messages(request):
    messages = ChatMessage.objects.all()
    messages_list = [{"sender": message.sender, "message": message.message, "timestamp": message.timestamp.strftime("%Y-%m-%d %H:%M:%S")} for message in messages]
    messages_json = json.dumps(messages_list)
    return HttpResponse(messages_json, content_type="application/json")
