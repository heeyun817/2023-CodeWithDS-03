from django.urls import path
from . import views

app_name="board"

urlpatterns = [
    #path('taxi/', views.calculate_taxi_fare, name='taxi'),
    path('create/', views.create, name='create'),
    path('copy/', views.taxi, name="copy"),
    path('map/', views.map, name="map"),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('proxy-request/', views.proxy_request, name='proxy_request'),
    path('update/<int:pk>/', views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    path("", views.list, name="list"),
    path('walkcreate/', views.walkcreate, name='walkcreate'),
    path('walkcopy/', views.walktaxi, name="walkcopy"),
    path('walkdetail/<int:pk>/', views.walkdetail, name="walkdetail"),
    path("walk", views.walklist, name="walklist"),
    path('walkupdate/<int:pk>/', views.walkupdate, name="walkupdate"),
    path('walkdelete/<int:pk>/', views.walkdelete, name="walkdelete"),
    path("walk/", views.walkroad, name="walk"),
    path("safemap/", views.map_view, name="map_view")

]
