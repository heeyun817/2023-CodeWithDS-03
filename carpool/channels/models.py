from django.db import models
from django.contrib.auth.models import User
from board.models import Board  # 이 부분은 게시물 모델의 위치에 맞게 수정



class ChatRoom(models.Model): #채팅방
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    #어디 글에 해당되는 채팅방인지
    user_group = models.ManyToManyField(User)
    #어떤 유저가 참여하는지 = 추가적으로 유저가 들어오고 나가는 것
    #해당 유저만 채팅할 수 있도록 만드는 것 필요할 듯

    #created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Chat Room for {self.board.s_title}"

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    chatRoom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    #어떤 채팅방의 댓글들인지에 대한 댓글인지 있으면 좋을 듯


    def __str__(self):
        return f"{self.sender}: {self.message}"


