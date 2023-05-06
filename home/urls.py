from django.urls import path
from home.views import home

app_name = 'example_app'

urlpatterns = [
    path('', home, name='home'),
]