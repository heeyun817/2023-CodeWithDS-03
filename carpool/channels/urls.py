from django.urls import path
from .views import chat_view, get_messages, send_message, create_chat_room, chat_view

app_name="channels"

urlpatterns = [
    path('', chat_view, name='chat'),
    path('get_messages/<int:pk>/', get_messages, name='get_messages'),
    path('send_message/<int:pk>/', send_message, name='send_message'),
    path('create_chat_room/<int:pk>/', create_chat_room, name='create_chat_room'),
    path('chat_view/<int:pk>/',chat_view, name="chat_room" ),

]