from django.db import models
from django.utils import timezone

# Create your models here.
class Board(models.Model):
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


    def __str__(self):
        return f'{self.s_title} - {self.d_title}'