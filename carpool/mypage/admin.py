from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)

# @admin.register(MatchRecord)
# class MatchRecordAdmin(admin.ModelAdmin):
#     list_display = ('user', 'board', 'matched_date', 'match')
#     list_filter = ('user', 'match')
#     search_fields = ('user__username', 'board__s_title', 'board__d_title')