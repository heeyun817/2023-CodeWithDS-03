from django.shortcuts import render, HttpResponse, redirect
from .models import ChatMessage
import json
from django.contrib.auth.models import User

def chat_view(request):
    messages = ChatMessage.objects.all()
    if request.method == "GET" :
      context = {'messages': messages}
    if request.method == "POST":
        sender = User.objects.get(pk = request.user.pk)  # Change this to the actual sender (e.g., user's username)
        message = request.POST.get("message")
        ChatMessage.objects.create(sender=sender, message=message)
        messages = ChatMessage.objects.all()
        return redirect("channels:chat", {'messages': messages})
    return render(request, 'chat.html', {'messages': messages})

def send_message(request):
    if request.method == "POST":
        sender = User.objects.get(pk = request.user.pk)  # Change this to the actual sender (e.g., user's username)
        message = request.POST.get("message")
        ChatMessage.objects.create(sender=sender, message=message)
        return HttpResponse("Message sent successfully.")
    return HttpResponse("Invalid request.")

def get_messages(request):
    messages = ChatMessage.objects.all()
    if request.method == "GET" :
      context = {'messages': messages}
    return render(request, 'messages.html', {'messages': messages})
