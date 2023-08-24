from django.db import models
#from django.contrib.auth.models import User
from accounts.models import User
from board.models import Board

#프로필 모델
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # 전화번호 필드 추가
    image = models.ImageField(upload_to='Files/%Y/%m/%d/', null=True, blank=True)
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# # 매칭 기록
# class Matching(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     board = models.ForeignKey(Board, on_delete=models.CASCADE)
#     # is_matched = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f'{self.user.username} - {self.board.s_title}'