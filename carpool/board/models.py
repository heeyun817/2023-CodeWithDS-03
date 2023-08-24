from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
from accounts.models import User
# Create your models here.
class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    s_title = models.CharField(max_length=20)
    #출발지
    d_title = models.CharField(max_length=20)
    #도착지
    date = models.DateTimeField(auto_now=False)
    #구하는 시간
    create = models.DateTimeField(default=timezone.now)
    #글 작성 시간
    content = models.TextField()
    star = models.BooleanField(default=False)
    #즐겨찾기
    people = models.PositiveIntegerField()
    #몇 명 모집?
    total = models.PositiveIntegerField()
    #얼마?
    completion = models.BooleanField(default=False)
    #구함 완료
    now_people = models.PositiveIntegerField()
    #현재까지 몇 명 구함
    member = models.ManyToManyField(User)


    def __str__(self):
        return f'{self.s_title} - {self.d_title}'


class WalkBoard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="walkuser")
    s_title = models.CharField(max_length=20)
    #출발지
    d_title = models.CharField(max_length=20)
    #도착지
    date = models.DateTimeField(auto_now=False)
    #구하는 시간
    create = models.DateTimeField(default=timezone.now)
    #글 작성 시간
    content = models.TextField()
    star = models.BooleanField(default=False)
    #즐겨찾기
    people = models.PositiveIntegerField()
    #몇 명 모집?
    completion = models.BooleanField(default=False)
    #구함 완료
    now_people = models.PositiveIntegerField()
    #현재까지 몇 명 구함
    member = models.ManyToManyField(User)


#     def __str__(self):
#         return f'{self.s_title} - {self.d_title}'