from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('edit_mypage/', views.edit_mypage, name='edit_mypage'),
    path('my_record/', views.my_record, name='my_record'),
    path('completed_boards/', views.completed_boards, name='completed_boards'),
    path('profile/<int:user_id>/', views.view_profile, name='view_profile'),
]


