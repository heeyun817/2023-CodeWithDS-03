from django.db import models
from django.contrib.auth.models import User

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    #어떤 포스트에 대한 댓글인지 있으면 좋을 듯

    def __str__(self):
        return f"{self.sender}: {self.message}"
