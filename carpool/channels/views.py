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

# def create_chat_room(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#
#     # 채팅방 생성 코드 작성
#     #chat_room = ChatRoom()
#     #chat_room.board = board
#     if (ChatRoom.objects.get(board=board) == None):
#         chat_room = ChatRoom.objects.create(board=board)
#     else:
#         chat_room = ChatRoom.objects.get(board=board)
#         chat_room.user_group.add(request.user)
#         board.member.add(request.user)
#         return redirect('channels:chat_room', pk=chat_room.pk)
#     # 유저 그룹에 해당 유저 추가
#     chat_room.user_group.add(request.user)
#     chat_room.user_group.add(board.user)
#     #본인이면 채ㅌ이방 생성하기 버튼 안 보이게 해야 함
#     chat_room.save()
#
#     #chat_room = ChatRoom.objects.create(board=board)  # 예시로 채팅방 생성 코드 작성
#
#     # 생성된 채팅방 페이지로 리다이렉트
#     return redirect('channels:chat_room', pk=chat_room.pk)


def create_chat_room(request, pk):
    board = get_object_or_404(Board, pk=pk)

    # 채팅방 생성 코드 작성
    # chat_room = ChatRoom()
    # chat_room.board = board
    if (ChatRoom.objects.get(board=board) == None):
        chat_room = ChatRoom.objects.create(board=board)
    else:
        chat_room = ChatRoom.objects.get(board=board)
        if (board.now_people) < board.people:
            chat_room.user_group.add(request.user)
            board.member.add(request.user)
            board.now_people = chat_room.user_group.count() - 1
            board.save()
            return redirect('channels:chat_room', pk=chat_room.pk)
        else:
            return redirect('board:list')
    # 유저 그룹에 해당 유저 추가
    chat_room.user_group.add(request.user)
    chat_room.user_group.add(board.user)
    # 본인이면 채ㅌ이방 생성하기 버튼 안 보이게 해야 함
    chat_room.save()

    # chat_room = ChatRoom.objects.create(board=board)  # 예시로 채팅방 생성 코드 작성

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

# 걷기

from .models import WalkChatMessage
from .models import WalkChatRoom

def walkchat_view(request):
    messages = WalkChatMessage.objects.all()
    if request.method == "GET" :
      context = {'messages': messages}
    if request.method == "POST":
        sender = User.objects.get(pk = request.user.pk)  # Change this to the actual sender (e.g., user's username)
        message = request.POST.get("message")
        WalkChatMessage.objects.create(sender=sender, message=message)
        messages = WalkChatMessage.objects.all()
        return redirect("channels:walkchat", {'messages': messages})
    return render(request, 'chat.html', {'messages': messages})

def walksend_message(request, pk):
    chatroom = WalkChatRoom.objects.get(pk=pk) #해당 채팅방 가져오기
    messages = WalkChatMessage.objects.filter(chatRoom=chatroom) #오류
    if request.method == "POST":
        sender = User.objects.get(pk = request.user.pk)  # Change this to the actual sender (e.g., user's username)
        message = request.POST.get("message")
        ChatMessage.objects.create(sender=sender, message=message, chatRoom=chatroom) #오류
        return HttpResponse("Message sent successfully.")
    return HttpResponse("Invalid request.")

def walkget_messages(request, pk):
    chatroom = WalkChatRoom.objects.get(pk=pk) #해당 채팅방 가져오기
    messages = WalkChatMessage.objects.filter(chatRoom=chatroom) #오류
    if request.method == "GET" :
      context = {'messages': messages}
    return render(request, 'messages.html', {'messages': messages, 'chatroom':chatroom})


# channels/views.py

from django.shortcuts import redirect, get_object_or_404
from .models import WalkChatRoom
from board.models import WalkBoard  # 이 부분은 게시물 모델의 위치에 맞게 수정

# def create_chat_room(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#
#     # 채팅방 생성 코드 작성
#     #chat_room = ChatRoom()
#     #chat_room.board = board
#     if (ChatRoom.objects.get(board=board) == None):
#         chat_room = ChatRoom.objects.create(board=board)
#     else:
#         chat_room = ChatRoom.objects.get(board=board)
#         chat_room.user_group.add(request.user)
#         board.member.add(request.user)
#         return redirect('channels:chat_room', pk=chat_room.pk)
#     # 유저 그룹에 해당 유저 추가
#     chat_room.user_group.add(request.user)
#     chat_room.user_group.add(board.user)
#     #본인이면 채ㅌ이방 생성하기 버튼 안 보이게 해야 함
#     chat_room.save()
#
#     #chat_room = ChatRoom.objects.create(board=board)  # 예시로 채팅방 생성 코드 작성
#
#     # 생성된 채팅방 페이지로 리다이렉트
#     return redirect('channels:chat_room', pk=chat_room.pk)


def walkcreate_chat_room(request, pk):
    board = get_object_or_404(WalkBoard, pk=pk)

    # 채팅방 생성 코드 작성
    # chat_room = ChatRoom()
    # chat_room.board = board
    if (WalkChatRoom.objects.get(board=board) == None):
        chat_room = WalkChatRoom.objects.create(board=board)
    else:
        chat_room = WalkChatRoom.objects.get(board=board)
        if (board.now_people) < board.people:
            chat_room.user_group.add(request.user)
            board.member.add(request.user)
            board.now_people = chat_room.user_group.count() - 1
            board.save()
            return redirect('channels:walkchat_room', pk=chat_room.pk)
        else:
            return redirect('board:walklist')
    # 유저 그룹에 해당 유저 추가
    chat_room.user_group.add(request.user)
    chat_room.user_group.add(board.user)
    # 본인이면 채ㅌ이방 생성하기 버튼 안 보이게 해야 함
    chat_room.save()

    # chat_room = ChatRoom.objects.create(board=board)  # 예시로 채팅방 생성 코드 작성

    # 생성된 채팅방 페이지로 리다이렉트
    return redirect('channels:walkchat_room', pk=chat_room.pk)


def walkchat_view(request, pk):
    chatroom = WalkChatRoom.objects.get(pk=pk) #해당 채팅방 가져오기
    messages = WalkChatMessage.objects.filter(chatRoom=chatroom)
    if request.method == "POST":
        sender = User.objects.get(pk = request.user.pk)  # Change this to the actual sender (e.g., user's username)
        message = request.POST.get("message")
        chatroom = chatroom
        ChatMessage.objects.create(sender=sender, message=message, chatRoom=chatroom)
        messages = WalkChatMessage.objects.filter(chatRoom=chatroom)
        return redirect("channels:walkchat_room", pk, {'messages': messages , 'chatroom':chatroom})
    return render(request, 'walkchat.html', {'messages': messages , 'chatroom':chatroom})


def walkupdate_people_count(request, pk):
    if request.method == "POST":
        chatroom = WalkChatRoom.objects.get(pk=pk)
        board = WalkBoard.objects.get(pk=chatroom.board.pk)
        if board.now_people >= board.people:
            return redirect("board:walklist")
        board.now_people += 1
        board.save()
        return HttpResponse("People count updated", status=200)
    return HttpResponse("Invalid request", status=400)