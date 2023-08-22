from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# 기존의 UserAdmin 상속 받기?
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined')  # 보여줄 필드 설정

# User 모델에 대한 Admin 클래스 등록
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
