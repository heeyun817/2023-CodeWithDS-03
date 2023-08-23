from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.search, name='search'),
    path('search_result/', views.search_result, name='search_result'),
]
