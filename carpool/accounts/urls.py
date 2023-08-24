from django.urls import path 
from . import views 
from accounts.views import signup

app_name = "accounts"

urlpatterns = [ 
	# path('signup/', views.signup, name='signup'),
    # path('verify_email/', views.verify_email, name="verify_email"),...

    path('signup/', views.signup, name='signup'),
    path('signup/verify_email/', views.verify_email, name="verify_email"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    # path('send_email/', views.send_mail, name='send_email')
]