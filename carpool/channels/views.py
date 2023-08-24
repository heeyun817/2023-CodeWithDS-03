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

def send_message(request, pk):
    chatroom = ChatRoom.objects.get(pk=pk) #해당 채팅방 가져오기
    messages = ChatMessage.objects.filter(chatRoom=chatroom)
    if request.method == "POST":
        sender = User.objects.get(pk = request.user.pk)  # Change this to the actual sender (e.g., user's username)
        message = request.POST.get("message")
        ChatMessage.objects.create(sender=sender, message=message, chatRoom=chatroom)
        return HttpResponse("Message sent successfully.")
    return HttpResponse("Invalid request.")

def get_messages(request, pk):
    chatroom = ChatRoom.objects.get(pk=pk) #해당 채팅방 가져오기
    messages = ChatMessage.objects.filter(chatRoom=chatroom)
    if request.method == "GET" :
      context = {'messages': messages}
    return render(request, 'messages.html', {'messages': messages, 'chatroom':chatroom})


# channels/views.py

from django.shortcuts import redirect, get_object_or_404
from .models import ChatRoom
from board.models import Board  # 이 부분은 게시물 모델의 위치에 맞게 수정

def create_chat_room(request, pk):
    board = get_object_or_404(Board, pk=pk)
    
    # 채팅방 생성 코드 작성
    #chat_room = ChatRoom()
    #chat_room.board = board
    if (ChatRoom.objects.get(board=board) == None):
        chat_room = ChatRoom.objects.create(board=board)
    else:
        chat_room = ChatRoom.objects.get(board=board)
        chat_room.user_group.add(request.user)
        board.member.add(request.user)
        return redirect('channels:chat_room', pk=chat_room.pk)
    # 유저 그룹에 해당 유저 추가
    chat_room.user_group.add(request.user)
    chat_room.user_group.add(board.user)
    #본인이면 채ㅌ이방 생성하기 버튼 안 보이게 해야 함
    chat_room.save()

    #chat_room = ChatRoom.objects.create(board=board)  # 예시로 채팅방 생성 코드 작성

    # 생성된 채팅방 페이지로 리다이렉트
    return redirect('channels:chat_room', pk=chat_room.pk)


def chat_view(request, pk):
    chatroom = ChatRoom.objects.get(pk=pk) #해당 채팅방 가져오기
    messages = ChatMessage.objects.filter(chatRoom=chatroom)
    if request.method == "POST":
        sender = User.objects.get(pk = request.user.pk)  # Change this to the actual sender (e.g., user's username)
        message = request.POST.get("message")
        chatroom = chatroom
        ChatMessage.objects.create(sender=sender, message=message, chatRoom=chatroom)
        messages = ChatMessage.objects.filter(chatRoom=chatroom)
        return redirect("channels:chat_room", pk, {'messages': messages , 'chatroom':chatroom})
    return render(request, 'chat.html', {'messages': messages , 'chatroom':chatroom})



def update_people_count(request, pk):
    if request.method == "POST":
        chatroom = ChatRoom.objects.get(pk=pk)
        board = Board.objects.get(pk=chatroom.board.pk)
        if board.now_people >= board.people:
            return redirect("board:list")
        board.now_people += 1
        board.save()
        return HttpResponse("People count updated", status=200)
    return HttpResponse("Invalid request", status=400)