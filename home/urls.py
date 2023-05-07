from django.urls import path
from home.views import home, register, login_user, logout_user, login_register

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('login_register/', login_register, name='login_register'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]