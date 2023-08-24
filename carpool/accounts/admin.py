from django.contrib import admin
from .models import User, Code

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'signup_date', 'password')  # 표시할 필드 지정

admin.site.register(Code)