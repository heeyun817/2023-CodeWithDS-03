from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    path('mypage/', views.mypage, name='mypage'),
    path('edit_mypage/', views.edit_mypage, name='edit_mypage'),
]


# from django.urls import path
# from . import views
#
# app_name = 'mypage'
#
# urlpatterns = [
#     path('', views.mypage, name='mypage'),
#     path('edit_profile/', views.edit_profile, name='edit_profile'),
# ]
