from django.urls import path
from .views import chat_view, get_messages, send_message, create_chat_room, chat_view, update_people_count
from .views import walkchat_view, walkget_messages, walksend_message, walkcreate_chat_room, walkchat_view, walkupdate_people_count
app_name="channels"

urlpatterns = [
    path('', chat_view, name='chat'),
    path('get_messages/<int:pk>/', get_messages, name='get_messages'),
    path('send_message/<int:pk>/', send_message, name='send_message'),
    path('create_chat_room/<int:pk>/', create_chat_room, name='create_chat_room'),
    path('chat_view/<int:pk>/',chat_view, name="chat_room" ),
    path('update_people_count/<int:pk>/', update_people_count, name="update_people_count" ),
    path('walk', chat_view, name='chat'),
    path('walkget_messages/<int:pk>/', walkget_messages, name='walkget_messages'),
    path('walksend_message/<int:pk>/', walksend_message, name='walksend_message'),
    path('walkcreate_chat_room/<int:pk>/', walkcreate_chat_room, name='walkcreate_chat_room'),
    path('walkchat_view/<int:pk>/',walkchat_view, name="walkchat_room" ),
    path('walkupdate_people_count/<int:pk>/', walkupdate_people_count, name="walkupdate_people_count" ),

]