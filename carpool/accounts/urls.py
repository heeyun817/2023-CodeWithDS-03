from django.urls import path 
from . import views 

app_name = "accounts"

urlpatterns = [ 
	# path('signup/', views.signup, name='signup'),
    # path('verify_email/', views.verify_email, name="verify_email"),

    path('home/signup/', views.signup, name='signup'),
    path('home/signup/verify_email/', views.verify_email, name="verify_email"),
    path('home/login/', views.login, name='login'),
    path('home/logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
]