from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # 전화번호 필드 추가
    image = models.ImageField(upload_to='Files/%Y/%m/%d/', null=True, blank=True)
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
