from django.urls import path
from home.views import home, register, login_user, logout_user

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]